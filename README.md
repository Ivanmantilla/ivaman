# SWMM biofilter cell example

This repository contains a ready-to-edit EPA SWMM input file for a **biofilter / bioretention cell**.

## Files

- `examples/biofilter_cell.inp` - a minimal SWMM 5.2 model that defines a bioretention LID control and deploys it inside a subcatchment.
- `scripts/run_swmm.sh` - a convenience wrapper for running the example with a local SWMM command-line executable.

## How to run this code

### Option 1: EPA SWMM desktop application

1. Install EPA SWMM 5.2 or newer on your computer.
2. Open the SWMM application.
3. Open `examples/biofilter_cell.inp`.
4. Click **Project -> Run Simulation**.
5. Review runoff, node, link, and LID results in the SWMM report/graph windows.

### Option 2: Command line

If you have a SWMM executable such as `swmm5` installed and available on your `PATH`, run:

```bash
bash scripts/run_swmm.sh
```

To run a different input file or choose custom output/report files:

```bash
bash scripts/run_swmm.sh examples/biofilter_cell.inp output/biofilter.out output/biofilter.rpt
```

The script will:

- create the output directory if needed
- call `swmm5` with the input, report, and binary output files
- print the generated file locations when the run finishes

## How to edit the biofilter

1. Review the `[LID_CONTROLS]` section to adjust the biofilter media, storage, and underdrain parameters.
2. Review the `[LID_USAGE]` section to change the number of units, footprint area, and percent of runoff captured.
3. Replace the example rainfall time series with your project rainfall data.
4. Update the subcatchment, junction, outfall, and conduit properties for your site geometry.

## Notes

- SWMM models a biofilter as a `BC` (bio-retention cell) LID control.
- The example uses a surface layer, engineered soil, gravel storage, and an underdrain.
- The values are reasonable starter inputs, not a final design.
