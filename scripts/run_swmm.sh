#!/usr/bin/env bash
set -euo pipefail

INPUT_FILE="${1:-examples/biofilter_cell.inp}"
OUT_FILE="${2:-output/biofilter_cell.out}"
RPT_FILE="${3:-output/biofilter_cell.rpt}"

if ! command -v swmm5 >/dev/null 2>&1; then
  echo "Error: 'swmm5' was not found on PATH." >&2
  echo "Install EPA SWMM and make sure the swmm5 CLI is available, then rerun this script." >&2
  exit 1
fi

if [[ ! -f "$INPUT_FILE" ]]; then
  echo "Error: input file '$INPUT_FILE' does not exist." >&2
  exit 1
fi

mkdir -p "$(dirname "$OUT_FILE")" "$(dirname "$RPT_FILE")"

swmm5 "$INPUT_FILE" "$RPT_FILE" "$OUT_FILE"

echo "SWMM run completed."
echo "Input : $INPUT_FILE"
echo "Report: $RPT_FILE"
echo "Output: $OUT_FILE"
