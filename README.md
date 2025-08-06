# NL Electricity System Simulation – Summer 2023

This project simulates the Dutch electricity system over one week in July 2023 using [PyPSA-Eur](https://github.com/PyPSA/pypsa-eur). The focus was on dispatch optimization using offshore wind, solar, and legacy thermal generation (oil, coal).

## Key Features
- Week-long simulation using ERA5 weather and ENTSO-E demand data
- Technologies: Offshore wind (DC), solar, and dispatchable oil
- Solver: HiGHS (linear optimization)
- Visualization: Daily dispatch vs demand comparison
- Tools: PyPSA-Eur, Snakemake, Python, Matplotlib

## Project Structure
