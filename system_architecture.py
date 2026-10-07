import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# -----------------------------------------
# Multi-Agent EV Charging System
# Architecture Diagram
# -----------------------------------------

fig, ax = plt.subplots(figsize=(12, 7))

ax.set_xlim(0, 12)
ax.set_ylim(0, 8)

# Function to create boxes
def add_box(x, y, width, height, text, fontsize=10):

    box = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.03",
        linewidth=1.5,
        edgecolor="black",
        facecolor="white"
    )

    ax.add_patch(box)

    ax.text(
        x + width / 2,
        y + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        fontweight="bold"
    )


# -----------------------------------------
# EV AGENTS
# -----------------------------------------

add_box(
    0.5, 5.8, 2.2, 1.0,
    "EV1 Agent\nBattery: 20%\nPriority: 4"
)

add_box(
    0.5, 3.9, 2.2, 1.0,
    "EV2 Agent\nBattery: 65%\nPriority: 1"
)

add_box(
    0.5, 2.0, 2.2, 1.0,
    "EV3 Agent\nBattery: 30%\nPriority: 3"
)


# -----------------------------------------
# A* DECISION MODULE
# -----------------------------------------

add_box(
    4.0, 4.0, 3.0, 1.8,
    "A* SEARCH\n\n"
    "g(n) + h(n) = f(n)\n"
    "State Evaluation\n"
    "Resource Allocation",
    fontsize=11
)


# -----------------------------------------
# CONSTRAINT CHECK
# -----------------------------------------

add_box(
    4.0, 1.2, 3.0, 1.5,
    "CONSTRAINT CHECK\n\n"
    "Available Slots\n"
    "Power Limit ≤ 70 kW"
)


# -----------------------------------------
# CHARGING STATION
# -----------------------------------------

add_box(
    8.0, 3.5, 3.0, 2.2,
    "CHARGING STATION\n\n"
    "2 Charging Slots\n"
    "Power Limit: 70 kW\n"
    "Time Management"
)


# -----------------------------------------
# OUTPUT
# -----------------------------------------

add_box(
    8.0, 0.8, 3.0, 1.5,
    "ALLOCATION RESULT\n\n"
    "Charging / Waiting /\n"
    "Completed"
)


# -----------------------------------------
# ARROWS
# -----------------------------------------

def add_arrow(x1, y1, x2, y2):

    arrow = FancyArrowPatch(
        (x1, y1),
        (x2, y2),
        arrowstyle="->",
        mutation_scale=15,
        linewidth=1.5
    )

    ax.add_patch(arrow)


# EV agents → A*
add_arrow(2.7, 6.3, 4.0, 5.1)
add_arrow(2.7, 4.4, 4.0, 4.8)
add_arrow(2.7, 2.5, 4.0, 4.2)

# A* → constraint checking
add_arrow(5.5, 4.0, 5.5, 2.7)

# Constraint → charging station
add_arrow(7.0, 2.0, 8.0, 4.0)

# A* → charging station
add_arrow(7.0, 4.9, 8.0, 4.9)

# Charging station → result
add_arrow(9.5, 3.5, 9.5, 2.3)

# -----------------------------------------
# TITLE
# -----------------------------------------

ax.set_title(
    "Multi-Agent EV Charging Station Management Architecture",
    fontsize=15,
    fontweight="bold"
)

# Remove axes
ax.set_xticks([])
ax.set_yticks([])

for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()

# Save image
plt.savefig(
    "system_architecture.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()