import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def rotate_point(x, y, cx, cy, angle):
    rad = math.radians(angle)
    cos_a, sin_a = math.cos(rad), math.sin(rad)
    x_rel, y_rel = x - cx, y - cy
    x_rot = x_rel * cos_a - y_rel * sin_a
    y_rot = x_rel * sin_a + y_rel * cos_a
    return round(cx + x_rot), round(cy + y_rot)

def draw_triangle(ax, x1, y1, x2, y2, x3, y3, color, label=None):
    tri = mpatches.Polygon(
        [(x1, y1), (x2, y2), (x3, y3)],
        fill=False, edgecolor=color, linewidth=2, label=label
    )
    ax.add_patch(tri)

print("=== Triangle Vertices ===")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
x3 = int(input("x3 = "))
y3 = int(input("y3 = "))

print("\n=== Rotation ===")
cx = int(input("pivot x = "))
cy = int(input("pivot y = "))
angle = float(input("angle (degrees) = "))

r1 = rotate_point(x1, y1, cx, cy, angle)
r2 = rotate_point(x2, y2, cx, cy, angle)
r3 = rotate_point(x3, y3, cx, cy, angle)

rad = math.radians(angle)
cos_a = round(math.cos(rad), 4)
sin_a = round(math.sin(rad), 4)

print(f"\n--- 2D Rotation ---")
print(f"Pivot: ({cx}, {cy})")
print(f"Angle: {angle} deg ({rad:.4f} rad)")
print(f"cos = {cos_a}, sin = {sin_a}")
print(f"\nRotation formula: x' = cx + (x-cx)*cos - (y-cy)*sin")
print(f"                 y' = cy + (x-cx)*sin + (y-cy)*cos")

print(f"\n{'Vertex':<8} {'Original':<16} {'Rotated':<16} {'Calculation':<30}")
print("-" * 72)
for (ox, oy), (rx, ry), label in [
    ((x1, y1), r1, "A"), ((x2, y2), r2, "B"), ((x3, y3), r3, "C")
]:
    x_rel, y_rel = ox - cx, oy - cy
    print(f"{label:<8} ({ox:<3},{oy:<3})        ({rx:<3},{ry:<3})        "
          f"({x_rel}*{cos_a} - {y_rel}*{sin_a}, {x_rel}*{sin_a} + {y_rel}*{cos_a})")

fig, ax = plt.subplots(figsize=(8, 7))
ax.set_title(f"2D Rotation: {angle} deg about ({cx},{cy})", color="white", fontsize=13)

all_x = [x1, x2, x3, r1[0], r2[0], r3[0], cx]
all_y = [y1, y2, y3, r1[1], r2[1], r3[1], cy]
margin = 30
max_r = max(max(all_x), max(all_y), -min(all_x), -min(all_y))
ax.set_xlim(-max_r - margin, max_r + margin)
ax.set_ylim(-max_r - margin, max_r + margin)
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)

ax.axhline(0, color="gray", linewidth=0.8, alpha=0.3)
ax.axvline(0, color="gray", linewidth=0.8, alpha=0.3)

draw_triangle(ax, x1, y1, x2, y2, x3, y3, "white", "Original")
draw_triangle(ax, r1[0], r1[1], r2[0], r2[1], r3[0], r3[1], "magenta", f"Rotated {angle} deg")

ax.scatter([x1, x2, x3], [y1, y2, y3], c="white", s=60, zorder=4, edgecolors="gray")
ax.scatter([r1[0], r2[0], r3[0]], [r1[1], r2[1], r3[1]], c="magenta", s=60, zorder=4, edgecolors="darkmagenta")
ax.scatter([cx], [cy], c="red", s=120, zorder=5, marker="*", edgecolors="darkred")
ax.annotate(f"Pivot({cx},{cy})", (cx, cy), xytext=(8, -12),
            textcoords="offset points", color="red", fontsize=10, fontweight="bold")

for (ox, oy), (rx, ry), label in [
    ((x1, y1), r1, "A"), ((x2, y2), r2, "B"), ((x3, y3), r3, "C")
]:
    ax.annotate(f"{label}({ox},{oy})", (ox, oy), xytext=(5, 8),
                textcoords="offset points", color="white", fontsize=9, fontweight="bold")
    ax.annotate(f"{label}'({rx},{ry})", (rx, ry), xytext=(5, 8),
                textcoords="offset points", color="magenta", fontsize=9, fontweight="bold")

info = (
    f"Pivot: ({cx},{cy})\n"
    f"Angle: {angle} deg\n"
    f"cos = {cos_a}, sin = {sin_a}"
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
