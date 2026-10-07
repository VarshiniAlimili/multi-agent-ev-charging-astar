import matplotlib.pyplot as plt

# -----------------------------------------
# A* State Space - EV Charging System
# -----------------------------------------

fig, ax = plt.subplots(figsize=(12, 7))

# Node positions
positions = {
    "(0,0,0)": (0, 3),
    "(1,0,0)": (2, 3),

    "(1,2,0)": (4, 4),
    "(1,0,2)": (4, 2),

    "(-1,0,2)": (6, 2),
    "(-1,1,2)": (8, 2),
    "(-1,1,-1)": (10, 2),
    "(-1,-1,-1)": (12, 2)
}

# Connections representing the search
edges = [
    ("(0,0,0)", "(1,0,0)"),
    ("(1,0,0)", "(1,2,0)"),
    ("(1,0,0)", "(1,0,2)"),
    ("(1,0,2)", "(-1,0,2)"),
    ("(-1,0,2)", "(-1,1,2)"),
    ("(-1,1,2)", "(-1,1,-1)"),
    ("(-1,1,-1)", "(-1,-1,-1)")
]

# Draw edges
for start, end in edges:

    x1, y1 = positions[start]
    x2, y2 = positions[end]

    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="->",
            linewidth=1.8
        )
    )

# Draw nodes
for state, (x, y) in positions.items():

    if state == "(0,0,0)":
        node_color = "lightgray"

    elif state == "(-1,-1,-1)":
        node_color = "lightgreen"

    elif state == "(1,2,0)":
        node_color = "lightyellow"

    else:
        node_color = "lightblue"

    ax.scatter(
        x, y,
        s=1800,
        facecolors=node_color,
        edgecolors="black",
        linewidths=1.5,
        zorder=3
    )

    ax.text(
        x, y,
        state,
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
        zorder=4
    )

# Mark the explored path
path = [
    "(0,0,0)",
    "(1,0,0)",
    "(1,0,2)",
    "(-1,0,2)",
    "(-1,1,2)",
    "(-1,1,-1)",
    "(-1,-1,-1)"
]

for i in range(len(path) - 1):

    x1, y1 = positions[path[i]]
    x2, y2 = positions[path[i + 1]]

    ax.plot(
        [x1, x2],
        [y1, y2],
        linestyle="--",
        linewidth=3
    )

# Labels
ax.text(
    2, 3.45,
    "Initial assignment",
    ha="center",
    fontsize=9
)

ax.text(
    4, 1.45,
    "A* selected",
    ha="center",
    fontsize=9
)

ax.text(
    4, 4.45,
    "Alternative state",
    ha="center",
    fontsize=9
)

ax.text(
    12, 1.45,
    "Goal State",
    ha="center",
    fontsize=9
)

# Title
ax.set_title(
    "A* State Space for Multi-Agent EV Charging",
    fontsize=15,
    fontweight="bold"
)

ax.set_xlabel("Search Progress")
ax.set_ylabel("State Space")

# Remove unnecessary axis values
ax.set_xticks([])
ax.set_yticks([])

# Grid
ax.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()

# Save for report
plt.savefig(
    "astar_state_space.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()