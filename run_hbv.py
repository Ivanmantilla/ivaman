# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:20:16 2026

@author: IVMA
"""

from importlib.util import find_spec
import subprocess
import sys

from hbv_snow import HBVSnowModel, HBVParams, HBVState


def install_missing_packages(package_names):
    missing_packages = [package for package in package_names if find_spec(package) is None]
    if not missing_packages:
        return

    install_command = [sys.executable, "-m", "pip", "install", *missing_packages]
    try:
        subprocess.run(install_command, check=True)
    except subprocess.CalledProcessError as exc:
        missing_list = ", ".join(missing_packages)
        raise SystemExit(
            "Unable to install required packages: "
            f"{missing_list}. Please install them manually and rerun the script."
        ) from exc


install_missing_packages(["matplotlib", "pandas"])

import matplotlib.pyplot as plt
import pandas as pd


# Example input data
temperatures = [-5.0, -3.0, -1.0, 1.0, 3.0, 2.0, -2.0]
precipitation = [10.0, 5.0, 8.0, 6.0, 0.0, 4.0, 3.0]

# Define parameters
params = HBVParams(
    tt=0.0,
    cfmax=3.5,
    cfr=0.05,
    cwh=0.1,
)

# Initialize model
model = HBVSnowModel(params=params)

# Run simulation
results = model.simulate(
    temperatures=temperatures,
    precipitation=precipitation,
    initial_state=HBVState(),
)

results_df = pd.DataFrame(results)
results_df.insert(0, "time_step", range(1, len(results_df) + 1))

# Print results
for step in results_df.itertuples(index=False):
    print(f"Step {step.time_step}")
    print(f"  Temp: {step.temperature} °C")
    print(f"  Prec: {step.precipitation} mm")
    print(f"  Snow storage: {step.snow_storage:.2f} mm")
    print(f"  Liquid water: {step.liquid_water:.2f} mm")
    print(f"  Outflow: {step.outflow:.2f} mm")
    print("-" * 30)

# Plot snow storage and outflow over time
fig, ax1 = plt.subplots(figsize=(8, 4.5))
ax1.plot(
    results_df["time_step"],
    results_df["snow_storage"],
    color="tab:blue",
    marker="o",
    linewidth=2,
    label="Snow storage",
)
ax1.set_xlabel("Time step")
ax1.set_ylabel("Snow storage (mm)", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:blue")
ax1.set_xticks(results_df["time_step"])
ax1.grid(True, linestyle="--", alpha=0.4)

ax2 = ax1.twinx()
ax2.bar(
    results_df["time_step"],
    results_df["outflow"],
    color="tab:orange",
    alpha=0.35,
    label="Outflow",
)
ax2.set_ylabel("Outflow (mm)", color="tab:orange")
ax2.tick_params(axis="y", labelcolor="tab:orange")

lines, labels = ax1.get_legend_handles_labels()
bars, bar_labels = ax2.get_legend_handles_labels()
ax1.legend(lines + bars, labels + bar_labels, loc="upper left")

plt.title("HBV snow storage and outflow over time")
fig.tight_layout()
plt.show()
