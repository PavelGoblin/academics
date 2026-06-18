import matplotlib.pyplot as plt
import numpy as np

n = int(input("Number of points (8 or 16): "))
cx = float(input("cx (center x) = "))
cy = float(input("cy (center y) = "))
x = float(input("x (from center) = "))
y = float(input("y (from center) = "))

adj = input("Adjust radius from point? (y/n): ").strip().lower()
if adj == "y":
    r = np.sqrt(x * x + y * y)
    print(f"  -> r = sqrt({x}² + {y}²) = {r}")
else:
    r = float(input("r = "))

if n == 8:
    pts_local = [
        (x, y), (-x, y), (x, -y), (-x, -y),
        (y, x), (-y, x), (y, -x), (-y, -x),
    ]
    pts_local = sorted(pts_local, key=lambda p: np.arctan2(p[1], p[0]))
elif n == 16:
    theta0 = np.arctan2(y, x)
    angles = [theta0 + i * np.pi / 8 for i in range(16)]
    pts_local = [(r * np.cos(a), r * np.sin(a)) for a in angles]
else:
    print("Only 8 or 16 are supported")
    exit()

pts_global = [(cx + px, cy + py) for px, py in pts_local]

print(f"\nCenter = ({cx}, {cy})")
print(f"Number of points = {n}")
print(f"Local point = ({x}, {y}) relative to center")
print(f"x² + y² = {x*x + y*y}, r² = {r*r}")
print(f"\n{'Point':<8} {'Local':<22} {'Global':<22}")
print("-" * 52)
for i, ((px, py), (gx, gy)) in enumerate(zip(pts_local, pts_global)):
    print(f"P{i:<6} ({px:<8.3f},{py:<8.3f})    ({gx:<8.3f},{gy:<8.3f})")

fig, ax = plt.subplots(figsize=(9, 9))

pts = np.array(pts_global)
all_vals = np.concatenate([pts.flatten(), [cx, cy, r]])
lim = float(np.max(np.abs(all_vals)) + 5)

ax.axhline(0, color="gray", linewidth=0.8, linestyle="--", alpha=0.4)
ax.axvline(0, color="gray", linewidth=0.8, linestyle="--", alpha=0.4)
ax.text(lim * 0.95, 0.3, "X", fontsize=10, color="gray", ha="right")
ax.text(0.3, lim * 0.95, "Y", fontsize=10, color="gray", ha="right")

ax.axhline(cy, color="black", linewidth=1)
ax.axvline(cx, color="black", linewidth=1)
ax.annotate("X' (through C)", (lim * 0.95, cy), fontsize=9, color="black",
            ha="right", va="bottom", fontweight="bold")
ax.annotate("Y' (through C)", (cx, lim * 0.95), fontsize=9, color="black",
            ha="left", va="top", fontweight="bold")

ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_aspect("equal")
ax.grid(True, alpha=0.15)
ax.set_title(f"{n}-Way Circle Symmetry — Center ({cx},{cy}),  Local Point ({x},{y}),  r={r:.3f}", fontsize=12)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_position(("data", cx))
ax.spines["bottom"].set_position(("data", cy))

colors = plt.cm.tab10(np.linspace(0, 1, n))

gxs = [gx for gx, gy in pts_global]
gys = [gy for gx, gy in pts_global]
ax.plot(gxs + [gxs[0]], gys + [gys[0]], "-", color="blue", alpha=0.5,
        linewidth=1.5, label=f"{n}-gon")

for (gx, gy), c in zip(pts_global, colors):
    ax.plot([cx, gx], [cy, gy], "--", color=c, alpha=0.15, linewidth=0.8)

for i, ((gx, gy), (px, py), c) in enumerate(zip(pts_global, pts_local, colors)):
    ax.scatter(gx, gy, color=[c], s=120, zorder=5, edgecolors="black", linewidth=0.8)
    ax.annotate(f"P{i}({gx:.2f},{gy:.2f})", (gx, gy), xytext=(8, 8),
                textcoords="offset points", fontsize=7, fontweight="bold",
                color=c, bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.7, edgecolor=c))

theta = np.linspace(0, 2 * np.pi, 500)
ax.plot(cx + r * np.cos(theta), cy + r * np.sin(theta), "-",
        color="red", alpha=0.4, linewidth=2, label=f"Circle r={r:.3f}")

ax.scatter(cx, cy, c="red", s=150, marker="*", edgecolors="darkred",
           linewidths=1.5, zorder=7)
ax.annotate(f"C({cx},{cy})", (cx, cy), xytext=(10, -15),
            textcoords="offset points", fontsize=11, fontweight="bold",
            color="darkred")

ax.legend(fontsize=10, loc="upper right")
plt.tight_layout()
plt.show()
