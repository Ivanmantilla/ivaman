# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:20:16 2026

@author: IVMA
"""

from hbv_snow import HBVSnowModel, HBVParams, HBVState

# Example input data
temperatures = [-5.0, -3.0, -1.0, 1.0, 3.0, 2.0, -2.0]
precipitation = [10.0, 5.0, 8.0, 6.0, 0.0, 4.0, 3.0]

# Define parameters
params = HBVParams(
    tt=0.0,
    cfmax=3.5,
    cfr=0.05,
    cwh=0.1
)

# Initialize model
model = HBVSnowModel(params=params)

# Run simulation
results = model.simulate(
    temperatures=temperatures,
    precipitation=precipitation,
    initial_state=HBVState()
)

# Print results
for i, step in enumerate(results, start=1):
    print(f"Step {i}")
    print(f"  Temp: {step['temperature']} °C")
    print(f"  Prec: {step['precipitation']} mm")
    print(f"  Snow storage: {step['snow_storage']:.2f} mm")
    print(f"  Liquid water: {step['liquid_water']:.2f} mm")
    print(f"  Outflow: {step['outflow']:.2f} mm")
    print("-" * 30)