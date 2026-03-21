

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class HBVParams:
    tt: float = 0.0      # temperature threshold for snow/rain (°C)
    cfmax: float = 3.5   # degree-day melt factor (mm/°C/time step)
    cfr: float = 0.05    # refreezing factor
    cwh: float = 0.1     # water holding capacity as fraction of snowpack


@dataclass
class HBVState:
    snow: float = 0.0    # solid snow storage (mm)
    water: float = 0.0   # liquid water stored in snowpack (mm)


class HBVSnowModel:
    def __init__(self, params: HBVParams):
        self.params = params

    def step(self, temp: float, prec: float, state: HBVState) -> Dict:
        tt = self.params.tt
        cfmax = self.params.cfmax
        cfr = self.params.cfr
        cwh = self.params.cwh

        snow = state.snow
        water = state.water

        # Partition precipitation
        if temp < tt:
            snowfall = prec
            rainfall = 0.0
        else:
            snowfall = 0.0
            rainfall = prec

        snow += snowfall
        water += rainfall

        # Melt
        melt = 0.0
        if temp > tt:
            melt = min(snow, cfmax * (temp - tt))
            snow -= melt
            water += melt

        # Refreezing
        refreeze = 0.0
        if temp < tt:
            refreeze = min(water, cfr * cfmax * (tt - temp))
            water -= refreeze
            snow += refreeze

        # Water holding capacity
        max_water = cwh * snow
        outflow = 0.0
        if water > max_water:
            outflow = water - max_water
            water = max_water

        new_state = HBVState(snow=snow, water=water)

        return {
            "temperature": temp,
            "precipitation": prec,
            "snowfall": snowfall,
            "rainfall": rainfall,
            "melt": melt,
            "refreeze": refreeze,
            "snow_storage": snow,
            "liquid_water": water,
            "outflow": outflow,
            "state": new_state,
        }

    def simulate(self, temperatures: List[float], precipitation: List[float], initial_state=None):
        if len(temperatures) != len(precipitation):
            raise ValueError("temperatures and precipitation must have the same length")

        state = initial_state if initial_state is not None else HBVState()
        results = []

        for temp, prec in zip(temperatures, precipitation):
            result = self.step(temp, prec, state)
            results.append(result)
            state = result["state"]

        return results