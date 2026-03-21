# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:24:47 2026

@author: IVMA
"""

# HBV Snow Model

This repository contains a simple Python implementation of the HBV snow routine.

## Files

- `hbv_snow.py` : HBV snow routine
- `run_hbv.py` : example script to run the model

## Processes included

- snowfall / rainfall separation
- snow accumulation
- degree-day snowmelt
- refreezing
- liquid water holding capacity
- snowpack outflow

## How to run

Run the file `run_hbv.py` in Spyder or with:

```bash
python run_hbv.py
```

The example script prints the simulated states, installs `matplotlib` and `pandas` if they are missing, and opens a Matplotlib figure showing snow storage and snowpack outflow over time.
