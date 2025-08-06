🇳🇱 NL Electricity System Simulation – Summer 2023
A week-long simulation of the Dutch power grid (July 2023) using PyPSA-Eur, focused on renewable integration and dispatch optimization.

🔍 Objective
Model and analyze how the Netherlands’ electricity demand can be met using a mix of offshore wind (DC), solar PV, and legacy thermal generation (oil, coal). This project was designed as a portfolio demonstrator for energy systems modeling.

⚙️ Key Features
- Timeframe: July 1–7, 2023
- Data sources:
  - ERA5 (weather)
  - ENTSO-E (electricity demand)
- Technologies modeled:
  - Offshore Wind (DC-connected)
  - Solar PV
  - Thermal (CCGT, oil, coal)
- Optimization:
  - Linear OPF using the HiGHS solver
  - PyPSA-Eur configuration adapted for single-country focus
- Visualization: 
  - Generator dispatch vs demand
  - Resource utilization over time

🛠 Tools & Stack
- PyPSA-Eur
- Snakemake
- Python (Pandas, Matplotlib)
- Git & GitHub

📁 Project Structure
nl-electricity-summer-2023/

├── config.yaml                                  # Custom configuration for NL, 2023, summer week

├── plots/                                       # Model output plots

├── result_analysis_script.py                    # Script to load, run, and plot results

├── resources/                                   # Docs, papers, links, or maps used as refs

├── results/                                     # Output files (networks, plots)

├── dispatch_plot.png                            # Dispatch vs demand visualizations

├── README.md                                    # You're here

└── .gitignore

📈 Sample Output

<img width="1200" height="600" alt="dispatch_plot" src="https://github.com/user-attachments/assets/5314f648-4028-4d4f-9427-be8b966257e9" />

🧠 Learnings
- Customized PyPSA-Eur for single-country modeling (NL)
- Resolved solver configuration, cutout retrieval, and dispatch issues
- Gained experience in scenario design, constraint formulation, and interpreting results

🚀 Future Improvements
- Include batteries and hydrogen electrolysis
- Add CO₂ cap optimization
- Use finer time resolution (e.g. hourly)
- Compare summer vs winter performance

📬 Contact
Feel free to reach out via GitHub or LinkedIn for questions, collaborations, or rants about PyPSA bugs.








