import matplotlib.pyplot as plt
import numpy as np

cx = int(input("cx (center x) = "))
cy = int(input("cy (center y) = "))
x = int(input("x (from center) = "))
y = int(input("y (from center) = "))
r = int(input("r = "))

pts_local = [
    (x, y), (-x, y), (x, -y), (-x, -y),
    (y, x), (-y, x), (y, -x), (-y, -x),
]

pts_global = [(cx+px, cy+py) for px, py in pts_local]

print(f"\nCenter = ({cx}, {cy})")
print(f"Local point = ({x}, {y}) relative to center")
print(f"x^2 + y^2 = {x*x + y*y}, r^2 = {r*r}")
print(f"\n{'Point':<8} {'Local':<14} {'Global':<14} {'Formula':<20}")
print("-"*56)
formulas = [
    "( x,  y)", "(-x,  y)", "( x, -y)", "(-x, -y)",
    "( y,  x)", "(-y,  x)", "( y, -x)", "(-y, -x)",
]
for i, ((px, py), (gx, gy), f) in enumerate(zip(pts_local, pts_global, formulas)):
    print(f"P{i:<6} ({px:<3},{py:<3})    ({gx:<3},{gy:<3})    cx+{f} -> ({gx},{gy})")

fig, ax = plt.subplots(figsize=(9, 9))

lim = max(abs(cx), abs(cy), abs(x), abs(y), r) + 5

ax.axhline(0, color="gray", linewidth=0.8, linestyle="--", alpha=0.4)
ax.axvline(0, color="gray", linewidth=0.8, linestyle="--", alpha=0.4)
ax.text(lim*0.95, 0.3, "X", fontsize=10, color="gray", ha="right")
ax.text(0.3, lim*0.95, "Y", fontsize=10, color="gray", ha="right")

ax.axhline(cy, color="black", linewidth=1)
ax.axvline(cx, color="black", linewidth=1)
ax.annotate(f"X' (through C)", (lim*0.95, cy), fontsize=9, color="black",
            ha="right", va="bottom", fontweight="bold")
ax.annotate(f"Y' (through C)", (cx, lim*0.95), fontsize=9, color="black",
            ha="left", va="top", fontweight="bold")

ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_aspect("equal")
ax.grid(True, alpha=0.15)
ax.set_title(f"8-Way Circle Symmetry — Center ({cx},{cy}),  Local Point ({x},{y}),  r={r}", fontsize=12)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_position(("data", cx))
ax.spines["bottom"].set_position(("data", cy))

colors = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12",
          "#9b59b6", "#1abc9c", "#e67e22", "#34495e"]

for i, ((gx, gy), (px, py), f, c) in enumerate(zip(pts_global, pts_local, formulas, colors)):
    ax.scatter(gx, gy, c=c, s=120, zorder=5, edgecolors="black", linewidth=0.8)
    ax.annotate(f"P{i}({gx},{gy})", (gx, gy), xytext=(8, 8),
                textcoords="offset points", fontsize=8, fontweight="bold",
                color=c, bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.7, edgecolor=c))
    ax.plot([cx, gx], [cy, gy], "--", color=c, alpha=0.2, linewidth=0.8)

theta = np.linspace(0, 2*np.pi, 500)
ax.plot(cx + r*np.cos(theta), cy + r*np.sin(theta), "-",
        color="red", alpha=0.6, linewidth=2, label=f"Circle r={r}")

ax.scatter(cx, cy, c="red", s=150, marker="*", edgecolors="darkred",
           linewidths=1.5, zorder=7)
ax.annotate(f"C({cx},{cy})", (cx, cy), xytext=(10, -15),
            textcoords="offset points", fontsize=11, fontweight="bold",
            color="darkred")

ax.legend(fontsize=10, loc="upper right")
plt.tight_layout()
plt.show()
