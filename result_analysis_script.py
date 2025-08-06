import pypsa
import matplotlib.pyplot as plt

n = pypsa.Network("pypsa-eur/results/nl-summer19-windsolar/networks/base_s_1_elec_.nc")

# Check what's in the network
print("Generators:\n", n.generators[["carrier", "bus", "p_nom", "p_nom_opt"]])
print("Loads:\n", n.loads)
print("Snapshots:", n.snapshots)

# Dispatch and demand
dispatch = n.generators_t.p
demand = n.loads_t.p_set

# Print a preview of the dispatch and demand
print("\nDispatch (head):")
print(dispatch.head())

print("\nDemand (head):")
print(demand.head())

# Plot only if data exists
if not dispatch.empty and not demand.empty:
    ax = dispatch.plot(title="Generator Dispatch (MW)", figsize=(12, 6))
    demand.sum(axis=1).plot(ax=ax, linestyle='--', color='black', label="Total Demand", linewidth=2)
    plt.legend()
    plt.ylabel("Power [MW]")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("\n⚠️ No dispatch or demand data to plot.")



print("--------------------------------------------------")
print("--------------------------------------------------")
print("--------------------------------------------------")



print(n.generators.p_nom_opt)
print(n.generators_t.p.head())
print(n.loads_t.p_set.head())
print(n.snapshots)
