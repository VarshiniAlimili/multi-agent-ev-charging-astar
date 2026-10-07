import matplotlib.pyplot as plt

# -----------------------------------------
# EV Charging Allocation - Working Case 1
# -----------------------------------------

fig, ax = plt.subplots(figsize=(10, 5))

# Charging schedule obtained from simulation
# Slot 1: EV1 charges from time 0 to 4
# Slot 1: EV2 charges from time 4 to 7
# Slot 2: EV3 charges from time 0 to 5

# EV1
ax.barh(
    1, 4,
    left=0,
    height=0.5,
    label="EV1"
)

# EV2
ax.barh(
    1, 3,
    left=4,
    height=0.5,
    label="EV2"
)

# EV3
ax.barh(
    2, 5,
    left=0,
    height=0.5,
    label="EV3"
)

# Labels inside bars
ax.text(2, 1, "EV1", ha="center", va="center")
ax.text(5.5, 1, "EV2", ha="center", va="center")
ax.text(2.5, 2, "EV3", ha="center", va="center")

# Axis labels
ax.set_xlabel("Charging Time Units")
ax.set_ylabel("Charging Slot")

# Y-axis
ax.set_yticks([1, 2])
ax.set_yticklabels(["Slot 1", "Slot 2"])

# X-axis
ax.set_xticks(range(0, 8))

# Title
ax.set_title(
    "Working Case 1: Multi-Agent EV Charging Allocation"
)

# Grid
ax.grid(True, linestyle="--", alpha=0.5)

# Add annotations
ax.text(
    6.8, 2.35,
    "Power Limit = 70 kW",
    ha="right"
)

ax.text(
    6.8, 2.1,
    "Available Slots = 2",
    ha="right"
)

# Legend
ax.legend(
    loc="upper right"
)

plt.tight_layout()

# Save image for report
plt.savefig(
    "ev_charging_allocation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()