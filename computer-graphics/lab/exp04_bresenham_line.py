import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    swapped = 0
    if dy > dx:
        dx, dy = dy, dx
        swapped = 1

    p = 2 * dy - dx
    x, y = x1, y1
    pixels = []
    steps_data = []

    for i in range(dx + 1):
        pixels.append((x, y))
        steps_data.append((i, x, y, p))

        while p >= 0:
            if swapped:
                x += sx
            else:
                y += sy
            p -= 2 * dx

        if swapped:
            y += sy
        else:
            x += sx
        p += 2 * dy

    return pixels, steps_data, swapped

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

pixels, steps_data, swapped = bresenham_line(x1, y1, x2, y2)

dx_abs = abs(x2 - x1)
dy_abs = abs(y2 - y1)

print(f"\nBresenham Line: ({x1},{y1}) -> ({x2},{y2})")
print(f"|dx| = {dx_abs}, |dy| = {dy_abs}")
print(f"sx = {'+1' if x1 < x2 else '-1'}, sy = {'+1' if y1 < y2 else '-1'}")
print(f"swapped = {swapped}  ({'dy>dx' if swapped else 'dx>=dy'})")
print(f"Initial p = 2*dy - dx = 2*{dy_abs} - {dx_abs} = {2*dy_abs - dx_abs}")
print(f"\n{'Step':<6} {'x':<6} {'y':<6} {'p':<8}")
print("-" * 28)

for step, x, y, p_val in steps_data:
    print(f"{step:<6} {x:<6} {y:<6} {p_val:<8}")

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Bresenham Line Algorithm (Integer Arithmetic)", color="white", fontsize=13)
ax.axhline(0, color="gray", linewidth=0.8, alpha=0.4)
ax.axvline(0, color="gray", linewidth=0.8, alpha=0.4)

margin = max(abs(x1), abs(x2), abs(y1), abs(y2)) + 30
ax.set_xlim(-margin, margin)
ax.set_ylim(-margin, margin)

colors = plt.cm.plasma_r([i / len(pixels) for i in range(len(pixels))])
for i, (px, py) in enumerate(pixels):
    ax.scatter(px, py, c=[colors[i]], s=40, zorder=3, edgecolors="white", linewidth=0.3)

ax.plot([x1, x2], [y1, y2], "r--", linewidth=1.2, alpha=0.5, label="True line")

ax.scatter([x1, x2], [y1, y2], c="red", s=100, zorder=5, edgecolors="white", linewidth=0.5)
ax.annotate(f"A({x1},{y1})", (x1, y1), xytext=(8, 8),
            textcoords="offset points", color="red", fontsize=10, fontweight="bold")
ax.annotate(f"B({x2},{y2})", (x2, y2), xytext=(8, 8),
            textcoords="offset points", color="red", fontsize=10, fontweight="bold")

info = (
    f"|dx| = {dx_abs}  |dy| = {dy_abs}\n"
    f"Initial p0 = {2*dy_abs - dx_abs}\n"
    f"swapped = {swapped}\n"
    f"Total pixels: {len(pixels)}"
)
ax.text(0.02, 0.98, info, transform=ax.transAxes,
        fontsize=9, verticalalignment="top", color="black",
        bbox=dict(boxstyle="round", facecolor="lightcyan", alpha=0.9))

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
