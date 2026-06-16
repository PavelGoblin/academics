import matplotlib.pyplot as plt

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

dx = x2 - x1
dy = y2 - y1
steps = max(abs(dx), abs(dy))
x_inc = dx / steps
y_inc = dy / steps

print(f"\nDDA Line: ({x1},{y1}) -> ({x2},{y2})")
print(f"dx = {dx}, dy = {dy}")
print(f"steps = max(|dx|,|dy|) = {steps}")
print(f"x_inc = dx/steps = {dx}/{steps} = {x_inc:.4f}")
print(f"y_inc = dy/steps = {dy}/{steps} = {y_inc:.4f}")

print(f"\n{'Step':<6} {'x':<10} {'y':<10} {'round(x)':<10} {'round(y)':<10}")
print("-" * 50)

x, y = float(x1), float(y1)
pixels = []
for i in range(steps + 1):
    rx, ry = round(x), round(y)
    pixels.append((rx, ry))
    print(f"{i:<6} {x:<10.4f} {y:<10.4f} {rx:<10} {ry:<10}")
    x += x_inc
    y += y_inc

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title(f"DDA Line Algorithm", color="white", fontsize=13)
ax.axhline(0, color="gray", linewidth=0.8, alpha=0.4)
ax.axvline(0, color="gray", linewidth=0.8, alpha=0.4)

margin = max(abs(x1), abs(x2), abs(y1), abs(y2)) + 30
ax.set_xlim(-margin, margin)
ax.set_ylim(-margin, margin)

xs, ys = zip(*pixels)
ax.scatter(xs, ys, c="yellow", s=30, label="DDA Pixels", zorder=3)
ax.plot([x1, x2], [y1, y2], "r--", linewidth=1.2, alpha=0.6, label="True line")

ax.scatter([x1, x2], [y1, y2], c="red", s=100, zorder=5, edgecolors="white", linewidth=0.5)
ax.annotate(f"A({x1},{y1})", (x1, y1), xytext=(8, 8),
            textcoords="offset points", color="red", fontsize=10, fontweight="bold")
ax.annotate(f"B({x2},{y2})", (x2, y2), xytext=(8, 8),
            textcoords="offset points", color="red", fontsize=10, fontweight="bold")

info = (
    f"dx = {dx}   dy = {dy}\n"
    f"steps = {steps}\n"
    f"x_inc = {x_inc:.4f}\n"
    f"y_inc = {y_inc:.4f}\n"
    f"Total pixels: {len(pixels)}"
)
ax.text(0.02, 0.98, info, transform=ax.transAxes,
        fontsize=9, verticalalignment="top", color="black",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.9))

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)
ax.set_aspect("equal")
ax.set_facecolor("#2b2b2b")
ax.tick_params(colors="white")
ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
fig.patch.set_facecolor("#2b2b2b")

plt.tight_layout()
plt.show()
