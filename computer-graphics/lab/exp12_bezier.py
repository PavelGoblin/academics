import matplotlib.pyplot as plt
import numpy as np

def bernstein(t, i, n):
    from math import comb
    return comb(n, i) * (t ** i) * ((1 - t) ** (n - i))

def bezier_curve(control_x, control_y, steps=100):
    ts = np.linspace(0, 1, steps + 1)
    u = 1 - ts
    b0 = u ** 3
    b1 = 3 * ts * u ** 2
    b2 = 3 * ts ** 2 * u
    b3 = ts ** 3

    px = (b0 * control_x[0] + b1 * control_x[1] + b2 * control_x[2] + b3 * control_x[3])
    py = (b0 * control_y[0] + b1 * control_y[1] + b2 * control_y[2] + b3 * control_y[3])
    return px, py

print("=== Cubic Bezier Curve ===")
print("Enter 4 control points:")
pts = []
for i in range(4):
    x = int(input(f"P{i} x = "))
    y = int(input(f"P{i} y = "))
    pts.append((x, y))

cx, cy = [p[0] for p in pts], [p[1] for p in pts]

print(f"\nControl points:")
for i, (x, y) in enumerate(pts):
    print(f"  P{i}: ({x}, {y})")

print(f"\n{'t':<8} {'B0(t)':<10} {'B1(t)':<10} {'B2(t)':<10} {'B3(t)':<10} {'X(t)':<10} {'Y(t)':<10}")
print("-" * 68)
for t_val in [i / 10 for i in range(0, 11)]:
    b = [bernstein(t_val, i, 3) for i in range(4)]
    x_t = sum(b[i] * cx[i] for i in range(4))
    y_t = sum(b[i] * cy[i] for i in range(4))
    print(f"{t_val:<8.2f} {b[0]:<10.4f} {b[1]:<10.4f} {b[2]:<10.4f} {b[3]:<10.4f} {x_t:<10.2f} {y_t:<10.2f}")

px, py = bezier_curve(cx, cy)

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Cubic Bezier Curve", color="white", fontsize=13)
ax.axhline(0, color="gray", linewidth=0.8, alpha=0.3)
ax.axvline(0, color="gray", linewidth=0.8, alpha=0.3)

all_x = cx + px.tolist()
all_y = cy + py.tolist()
margin = 30
ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
ax.set_ylim(min(all_y) - margin, max(all_y) + margin)
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)

ax.plot(cx, cy, color="white", linewidth=1.5, linestyle="--", label="Control polygon")
ax.scatter(cx, cy, c="red", s=80, zorder=5, edgecolors="white")
for i, (x, y) in enumerate(pts):
    ax.annotate(f"P{i}({x},{y})", (x, y), xytext=(8, 8),
                textcoords="offset points", color="red", fontsize=10, fontweight="bold")

ax.plot(px, py, color="yellow", linewidth=2.5, label="Bezier curve")

colors = plt.cm.plasma(np.linspace(0, 1, 11))
for i, t_val in enumerate([i / 10 for i in range(0, 11)]):
    b = [bernstein(t_val, i, 3) for i in range(4)]
    x_t = sum(b[i] * cx[i] for i in range(4))
    y_t = sum(b[i] * cy[i] for i in range(4))
    ax.scatter(x_t, y_t, c=[colors[i]], s=40, zorder=4, edgecolors="white", linewidth=0.5)
    if i % 2 == 0:
        ax.annotate(f"t={t_val:.1f}", (x_t, y_t), xytext=(5, -12),
                    textcoords="offset points", fontsize=7, color="white", alpha=0.7)

info = (
    f"4 control points\n"
    f"Cubic Bernstein basis\n"
    f"Dots = t at 0.0, 0.1, ..., 1.0"
)
ax.text(0.02, 0.98, info, transform=ax.transAxes,
        fontsize=10, verticalalignment="top", color="black",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.9))

ax.set_xlabel("X", color="white")
ax.set_ylabel("Y", color="white")
ax.legend(fontsize=9, loc="upper left")
ax.set_facecolor("#2b2b2b")
ax.tick_params(colors="white")
ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
fig.patch.set_facecolor("#2b2b2b")

plt.tight_layout()
plt.show()
