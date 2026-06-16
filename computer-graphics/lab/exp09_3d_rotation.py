import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rotate_about_axis(point, a1, a2, angle):
    px = point[0] - a1[0]
    py = point[1] - a1[1]
    pz = point[2] - a1[2]

    ax = a2[0] - a1[0]
    ay = a2[1] - a1[1]
    az = a2[2] - a1[2]

    length = math.sqrt(ax*ax + ay*ay + az*az)
    ux, uy, uz = ax/length, ay/length, az/length

    rad = math.radians(angle)
    cos_a, sin_a = math.cos(rad), math.sin(rad)

    dot = px*ux + py*uy + pz*uz
    cross_x = uy*pz - uz*py
    cross_y = uz*px - ux*pz
    cross_z = ux*py - uy*px

    new_x = px*cos_a + cross_x*sin_a + ux*dot*(1 - cos_a)
    new_y = py*cos_a + cross_y*sin_a + uy*dot*(1 - cos_a)
    new_z = pz*cos_a + cross_z*sin_a + uz*dot*(1 - cos_a)

    return (round(new_x + a1[0], 2), round(new_y + a1[1], 2), round(new_z + a1[2], 2))

def draw_cube_3d(ax, vertices, color, label=None):
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    xs, ys, zs = zip(*vertices)
    for i, j in edges:
        ax.plot3D(*zip(vertices[i], vertices[j]), color=color, linewidth=1.5)
    ax.scatter(xs, ys, zs, c=color, s=40, label=label)

print("=== 3D Rotation About Arbitrary Axis ===")
print("Enter cube center:")
ccx = int(input("center x = "))
ccy = int(input("center y = "))
ccz = int(input("center z = "))
half = int(input("half-size (edge = 2*half) = "))

cube = [
    (ccx - half, ccy - half, ccz - half),
    (ccx + half, ccy - half, ccz - half),
    (ccx + half, ccy + half, ccz - half),
    (ccx - half, ccy + half, ccz - half),
    (ccx - half, ccy - half, ccz + half),
    (ccx + half, ccy - half, ccz + half),
    (ccx + half, ccy + half, ccz + half),
    (ccx - half, ccy + half, ccz + half),
]

print("\nRotation axis (two points):")
ax1_x = int(input("axis point1 x = "))
ax1_y = int(input("axis point1 y = "))
ax1_z = int(input("axis point1 z = "))
ax2_x = int(input("axis point2 x = "))
ax2_y = int(input("axis point2 y = "))
ax2_z = int(input("axis point2 z = "))

angle = float(input("rotation angle (degrees) = "))

a1 = (ax1_x, ax1_y, ax1_z)
a2 = (ax2_x, ax2_y, ax2_z)

rotated = [rotate_about_axis(v, a1, a2, angle) for v in cube]

print(f"\n--- 3D Rotation ---")
print(f"Center: ({ccx},{ccy},{ccz}), half-size: {half}")
print(f"Axis: ({ax1_x},{ax1_y},{ax1_z}) -> ({ax2_x},{ax2_y},{ax2_z})")
print(f"Angle: {angle} deg")
print(f"\n{'Vertex':<8} {'Original':<30} {'Rotated':<30}")
print("-" * 70)
for i in range(8):
    print(f"V{i:<6} ({cube[i][0]:<5},{cube[i][1]:<5},{cube[i][2]:<5})       "
          f"({rotated[i][0]:<6},{rotated[i][1]:<6},{rotated[i][2]:<6})")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.set_title(f"3D Rotation: {angle} deg About Custom Axis", color="white", fontsize=13)

draw_cube_3d(ax, cube, "white", "Original")
draw_cube_3d(ax, rotated, "yellow", f"Rotated {angle} deg")

axis_xs = [ax1_x, ax2_x]
axis_ys = [ax1_y, ax2_y]
axis_zs = [ax1_z, ax2_z]
ax.plot3D(axis_xs, axis_ys, axis_zs, "r--", linewidth=2, label="Rotation axis")
ax.scatter([ax1_x, ax2_x], [ax1_y, ax2_y], [ax1_z, ax2_z],
           c="red", s=60, marker="*", zorder=5)

info = (
    f"Axis: ({ax1_x},{ax1_y},{ax1_z})->({ax2_x},{ax2_y},{ax2_z})\n"
    f"Angle: {angle} deg"
)
ax.text(0.02, 0.98, 0.98, info, transform=ax.transAxes,
        fontsize=10, verticalalignment="top", color="black",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.9))

ax.set_xlabel("X", color="white")
ax.set_ylabel("Y", color="white")
ax.set_zlabel("Z", color="white")
ax.legend(fontsize=9, loc="lower right")
ax.set_facecolor("#2b2b2b")
fig.patch.set_facecolor("#2b2b2b")
ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
ax.zaxis.label.set_color("white")
ax.title.set_color("white")
ax.tick_params(colors="white")

plt.tight_layout()
plt.show()
