import matplotlib.pyplot as plt

# -----------------------------------------
# EV Urgency Comparison
# -----------------------------------------

ev_names = ["EV1", "EV2", "EV3"]

battery = [20, 65, 30]
priority = [4, 1, 3]

# Urgency formula
urgency = []

for i in range(len(ev_names)):

    value = (100 - battery[i]) + (20 * priority[i])

    urgency.append(value)

# Create graph
fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(
    ev_names,
    urgency,
    edgecolor="black"
)

# Display values above bars
for bar, value in zip(bars, urgency):

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + 3,
        str(value),
        ha="center",
        fontweight="bold"
    )

# Labels
ax.set_xlabel("EV Agents")
ax.set_ylabel("Urgency Score")

ax.set_title(
    "EV Agent Urgency Comparison",
    fontweight="bold"
)

ax.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

# Save for report
plt.savefig(
    "ev_urgency_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()