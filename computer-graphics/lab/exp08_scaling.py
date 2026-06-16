import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def scale_point(x, y, fx, fy, sx, sy):
    return round(fx + (x - fx) * sx), round(fy + (y - fy) * sy)

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

print("\n=== Scaling ===")
fx = int(input("fixed point x = "))
fy = int(input("fixed point y = "))
sx = float(input("scale x (sx) = "))
sy = float(input("scale y (sy) = "))

s1 = scale_point(x1, y1, fx, fy, sx, sy)
s2 = scale_point(x2, y2, fx, fy, sx, sy)
s3 = scale_point(x3, y3, fx, fy, sx, sy)

print(f"\n--- 2D Scaling ---")
print(f"Fixed point: ({fx}, {fy})")
print(f"Scale factors: sx={sx}, sy={sy}")
print(f"\nFormula: x' = fx + (x - fx) * sx")
print(f"         y' = fy + (y - fy) * sy")

print(f"\n{'Vertex':<8} {'Original':<16} {'Scaled':<16} {'Calculation':<30}")
print("-" * 72)
for (ox, oy), (sx_p, sy_p), label in [
    ((x1, y1), s1, "A"), ((x2, y2), s2, "B"), ((x3, y3), s3, "C")
]:
    print(f"{label:<8} ({ox:<3},{oy:<3})        ({sx_p:<3},{sy_p:<3})        "
          f"({ox}-{fx})*{sx}, ({oy}-{fy})*{sy})")

fig, ax = plt.subplots(figsize=(8, 7))
ax.set_title(f"2D Scaling: sx={sx}, sy={sy} about ({fx},{fy})", color="white", fontsize=13)

all_x = [x1, x2, x3, s1[0], s2[0], s3[0], fx]
all_y = [y1, y2, y3, s1[1], s2[1], s3[1], fy]
margin = 30 + max(
    max(all_x) - min(all_x), max(all_y) - min(all_y)
) // 2

ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
ax.set_ylim(min(all_y) - margin, max(all_y) + margin)
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)

ax.axhline(0, color="gray", linewidth=0.8, alpha=0.3)
ax.axvline(0, color="gray", linewidth=0.8, alpha=0.3)

draw_triangle(ax, x1, y1, x2, y2, x3, y3, "white", "Original")
draw_triangle(ax, s1[0], s1[1], s2[0], s2[1], s3[0], s3[1], "lime", f"Scaled (sx={sx}, sy={sy})")

ax.scatter([x1, x2, x3], [y1, y2, y3], c="white", s=60, zorder=4, edgecolors="gray")
ax.scatter([s1[0], s2[0], s3[0]], [s1[1], s2[1], s3[1]], c="lime", s=60, zorder=4, edgecolors="darkgreen")
ax.scatter([fx], [fy], c="red", s=120, zorder=5, marker="*", edgecolors="darkred")
ax.annotate(f"Fixed({fx},{fy})", (fx, fy), xytext=(8, -12),
            textcoords="offset points", color="red", fontsize=10, fontweight="bold")

for (ox, oy), (rx, ry), label in [
    ((x1, y1), s1, "A"), ((x2, y2), s2, "B"), ((x3, y3), s3, "C")
]:
    ax.annotate(f"{label}({ox},{oy})", (ox, oy), xytext=(5, 8),
                textcoords="offset points", color="white", fontsize=9, fontweight="bold")
    ax.annotate(f"{label}'({rx},{ry})", (rx, ry), xytext=(5, 8),
                textcoords="offset points", color="lime", fontsize=9, fontweight="bold")

info = (
    f"Fixed point: ({fx},{fy})\n"
    f"sx = {sx}, sy = {sy}\n"
    f"x' = fx + (x-fx)*sx\n"
    f"y' = fy + (y-fy)*sy"
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
