import matplotlib.pyplot as plt

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

dx = x2 - x1
dy = y2 - y1

print(f"\nSlope-Intercept Line: ({x1},{y1}) -> ({x2},{y2})")
print(f"dx = {dx}, dy = {dy}")

pixels = []

if dx == 0:
    print("Vertical line (dx=0)")
    m_str = "undefined"
    c_str = "N/A"
    y_start, y_end = min(y1, y2), max(y1, y2)
    for y in range(y_start, y_end + 1):
        pixels.append((x1, y))
else:
    m = dy / dx
    c = y1 - m * x1
    m_str = f"{m:.4f}"
    c_str = f"{c:.4f}"
    print(f"m = dy/dx = {dy}/{dx} = {m_str}")
    print(f"c = y1 - m*x1 = {y1} - ({m_str})*{x1} = {c_str}")
    print(f"Equation: y = {m_str}x + {c_str}")

    print(f"\n{'Step':<6} {'x':<6} {'y_exact':<12} {'y_rounded':<10}")
    print("-" * 36)

    if abs(dx) >= abs(dy):
        x_start, x_end = min(x1, x2), max(x1, x2)
        for i, x in enumerate(range(x_start, x_end + 1)):
            y_exact = m * x + c
            y_round = round(y_exact)
            pixels.append((x, y_round))
            print(f"{i:<6} {x:<6} {y_exact:<12.4f} {y_round:<10}")
    else:
        y_start, y_end = min(y1, y2), max(y1, y2)
        for i, y in enumerate(range(y_start, y_end + 1)):
            x_exact = (y - c) / m
            x_round = round(x_exact)
            pixels.append((x_round, y))
            print(f"{i:<6} {y:<6} {x_exact:<12.4f} {x_round:<10}")

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title(f"Slope-Intercept: y = {m_str}x + {c_str}", color="white", fontsize=13)
ax.axhline(0, color="gray", linewidth=0.8, alpha=0.4)
ax.axvline(0, color="gray", linewidth=0.8, alpha=0.4)

margin = max(abs(x1), abs(x2), abs(y1), abs(y2)) + 30
ax.set_xlim(-margin, margin)
ax.set_ylim(-margin, margin)

xs, ys = zip(*pixels)
ax.scatter(xs, ys, c="yellow", s=30, label="Line pixels", zorder=3)
ax.plot([x1, x2], [y1, y2], "r--", linewidth=1.2, alpha=0.6, label="True line")

ax.scatter([x1, x2], [y1, y2], c="red", s=100, zorder=5, edgecolors="white", linewidth=0.5)
ax.annotate(f"A({x1},{y1})", (x1, y1), xytext=(8, 8),
            textcoords="offset points", color="red", fontsize=10, fontweight="bold")
ax.annotate(f"B({x2},{y2})", (x2, y2), xytext=(8, 8),
            textcoords="offset points", color="red", fontsize=10, fontweight="bold")

info = (
    f"dx = {dx}   dy = {dy}\n"
    f"m = {m_str}\n"
    f"c = {c_str}\n"
    f"Equation: y = {m_str}x + {c_str}\n"
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
