import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def draw_triangle(ax, x1, y1, x2, y2, x3, y3, color, label=None):
    tri = mpatches.Polygon(
        [(x1, y1), (x2, y2), (x3, y3)],
        fill=False, edgecolor=color, linewidth=2, label=label
    )
    ax.add_patch(tri)

print("=== Original Triangle ===")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
x3 = int(input("x3 = "))
y3 = int(input("y3 = "))

print("\n=== Translation Vector ===")
tx = int(input("tx = "))
ty = int(input("ty = "))

nx1, ny1 = x1 + tx, y1 + ty
nx2, ny2 = x2 + tx, y2 + ty
nx3, ny3 = x3 + tx, y3 + ty

print(f"\n--- 2D Translation ---")
print(f"Original Triangle: ({x1},{y1}), ({x2},{y2}), ({x3},{y3})")
print(f"Translation vector: tx={tx}, ty={ty}")

print(f"\n{'Vertex':<8} {'Original':<16} {'Translated':<16}")
print("-" * 42)
print(f"{'A':<8} ({x1:<3},{y1:<3})        ({nx1:<3},{ny1:<3})")
print(f"{'B':<8} ({x2:<3},{y2:<3})        ({nx2:<3},{ny2:<3})")
print(f"{'C':<8} ({x3:<3},{y3:<3})        ({nx3:<3},{ny3:<3})")

fig, ax = plt.subplots(figsize=(8, 7))
ax.set_title(f"2D Translation: tx={tx}, ty={ty}", color="white", fontsize=13)

all_x = [x1, x2, x3, nx1, nx2, nx3]
all_y = [y1, y2, y3, ny1, ny2, ny3]
margin = 30
ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
ax.set_ylim(min(all_y) - margin, max(all_y) + margin)
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)

ax.axhline(0, color="gray", linewidth=0.8, alpha=0.3)
ax.axvline(0, color="gray", linewidth=0.8, alpha=0.3)

draw_triangle(ax, x1, y1, x2, y2, x3, y3, "white", "Original")
draw_triangle(ax, nx1, ny1, nx2, ny2, nx3, ny3, "cyan", f"Translated (tx={tx}, ty={ty})")

ax.scatter([x1, x2, x3], [y1, y2, y3], c="white", s=60, zorder=4, edgecolors="gray")
ax.scatter([nx1, nx2, nx3], [ny1, ny2, ny3], c="cyan", s=60, zorder=4, edgecolors="darkcyan")

for (ox, oy), (nx, ny), label in [
    ((x1, y1), (nx1, ny1), "A"), ((x2, y2), (nx2, ny2), "B"), ((x3, y3), (nx3, ny3), "C")
]:
    ax.annotate(f"{label}({ox},{oy})", (ox, oy), xytext=(5, 8),
                textcoords="offset points", color="white", fontsize=9, fontweight="bold")
    ax.annotate(f"{label}'({nx},{ny})", (nx, ny), xytext=(5, 8),
                textcoords="offset points", color="cyan", fontsize=9, fontweight="bold")
    ax.annotate("", xy=(nx, ny), xytext=(ox, oy),
                arrowprops=dict(arrowstyle="->", color="yellow", lw=1.5, alpha=0.6))

info = (
    f"Translation: (x', y') = (x + tx, y + ty)\n"
    f"x' = x + {tx}\n"
    f"y' = y + {ty}"
)
ax.text(0.02, 0.98, info, transform=ax.transAxes,
        fontsize=10, verticalalignment="top", color="black",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.9))

ax.set_xlabel("X", color="white")
ax.set_ylabel("Y", color="white")
ax.legend(fontsize=9, loc="lower right")
ax.set_facecolor("#2b2b2b")
ax.tick_params(colors="white")
ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
fig.patch.set_facecolor("#2b2b2b")

plt.tight_layout()
plt.show()
