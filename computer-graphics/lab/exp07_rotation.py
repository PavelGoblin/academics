import sys
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.widgets import Slider, Button
from matplotlib.patches import FancyArrowPatch

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def rotate_point(x, y, cx, cy, angle_deg):
    rad = math.radians(angle_deg)
    cos_a, sin_a = math.cos(rad), math.sin(rad)
    x_rel, y_rel = x - cx, y - cy
    x_rot = x_rel * cos_a - y_rel * sin_a
    y_rot = x_rel * sin_a + y_rel * cos_a
    return (cx + x_rot, cy + y_rot)


def get_arc_points(x, y, cx, cy, angle_deg, num=60):
    dx, dy = x - cx, y - cy
    radius = math.hypot(dx, dy)
    if radius < 1e-10:
        return [(x, y)] * 2
    start_rad = math.atan2(dy, dx)
    end_rad = start_rad + math.radians(angle_deg)
    pts = []
    for i in range(num + 1):
        t = i / num
        r = start_rad + (end_rad - start_rad) * t
        pts.append((cx + radius * math.cos(r), cy + radius * math.sin(r)))
    return pts


def smart_offset(vx, vy, verts, dist=20, angle_offset=0):
    sx = sum(v[0] for v in verts) / len(verts)
    sy = sum(v[1] for v in verts) / len(verts)
    dx = vx - sx
    dy = vy - sy
    mag = math.hypot(dx, dy)
    if mag < 1:
        return (dist, -dist)
    off_rad = math.radians(angle_offset)
    cos_a, sin_a = math.cos(off_rad), math.sin(off_rad)
    return ((dx * cos_a - dy * sin_a) / mag * dist,
            (dx * sin_a + dy * cos_a) / mag * dist)


def format_vertex_calc(ox, oy, cx, cy, cos_v, sin_v):
    dx = ox - cx
    dy = oy - cy
    xp = cx + dx * cos_v - dy * sin_v
    yp = cy + dx * sin_v + dy * cos_v
    return (
        f"  x' = cx + (x-cx)*cos\u03b8 - (y-cy)*sin\u03b8\n"
        f"     = {cx} + ({dx})*{cos_v:.4f} - ({dy})*{sin_v:.4f}\n"
        f"     = {xp:.2f}\n"
        f"  y' = cy + (x-cx)*sin\u03b8 + (y-cy)*cos\u03b8\n"
        f"     = {cy} + ({dx})*{sin_v:.4f} + ({dy})*{cos_v:.4f}\n"
        f"     = {yp:.2f}"
    )


# ============================================================
# USER INPUT
# ============================================================
print("=" * 60)
print("  2D ROTATION — INTERACTIVE VISUALIZATION")
print("=" * 60)

print("\n--- Shape Selection ---")
print("  1. Straight Line (2 vertices)")
print("  2. Triangle      (3 vertices)")
print("  3. Rectangle     (4 corners)")
shape_choice = int(input("  Choose shape (1/2/3): "))

print("\n--- Rotation Direction ---")
print("  1. Anticlockwise (positive angle)")
print("  2. Clockwise     (negative angle)")
dir_choice = int(input("  Choose direction (1/2): "))
dir_sign = 1 if dir_choice == 1 else -1
dir_name = "Anticlockwise" if dir_choice == 1 else "Clockwise"

shape_name = {1: "Line", 2: "Triangle", 3: "Rectangle"}[shape_choice]
n_verts = {1: 2, 2: 3, 3: 4}[shape_choice]
vert_labels = {1: ["P\u2081", "P\u2082"],
               2: ["A", "B", "C"],
               3: ["P\u2081", "P\u2082", "P\u2083", "P\u2084"]}[shape_choice]

print(f"\n--- {shape_name} Vertices ---")
verts = []
for i in range(n_verts):
    x = int(input(f"  {vert_labels[i]} x = "))
    y = int(input(f"  {vert_labels[i]} y = "))
    verts.append((x, y))

print(f"\n--- Rotation Point ---")
print("  1. Origin (0, 0)")
print("  2. Center of Shape (auto)")
print("  3. Custom Point")
rot_pt_choice = int(input("  Choose rotation point (1/2/3): "))

if rot_pt_choice == 1:
    cx, cy = 0, 0
    rot_pt_name = "Origin (0,0)"
elif rot_pt_choice == 2:
    cx = round(sum(v[0] for v in verts) / n_verts)
    cy = round(sum(v[1] for v in verts) / n_verts)
    rot_pt_name = f"Center ({cx}, {cy})"
else:
    cx = int(input("  pivot x = "))
    cy = int(input("  pivot y = "))
    rot_pt_name = f"Custom ({cx}, {cy})"

print(f"\n--- Angle ---")
raw_angle = float(input("  angle (degrees) = "))
# Apply direction: anticlockwise = +angle, clockwise = -angle
angle = raw_angle * dir_sign

rotated = [rotate_point(x, y, cx, cy, angle) for (x, y) in verts]

rad = math.radians(angle)
cos_a = math.cos(rad)
sin_a = math.sin(rad)

# ---------------------------------------------------------------
# CONSOLE OUTPUT
# ---------------------------------------------------------------
print(f"\n{'=' * 60}")
print(f"  RESULTS")
print(f"{'=' * 60}")
print(f"  Shape     : {shape_name}")
print(f"  Direction : {dir_name}")
print(f"  Rot point : {rot_pt_name}")
print(f"  Angle     : {abs(angle)}\u00b0 ({abs(rad):.4f} rad) {dir_name.lower()}")
print(f"  cos\u03b8 = {cos_a:.4f}")
print(f"  sin\u03b8 = {sin_a:.4f}")
print(f"\n  Rotation Matrix:")
print(f"  [cos\u03b8  -sin\u03b8]     [{cos_a:.4f}  {-sin_a:.4f}]")
print(f"  [sin\u03b8   cos\u03b8]     [{sin_a:.4f}   {cos_a:.4f}]")
print(f"\n  {'Pt':<4} {'Original':<20} {'Rotated':<20}")
print(f"  {'-' * 44}")
for (ox, oy), (rx, ry), lbl in zip(verts, rotated, vert_labels):
    print(f"  {lbl:<4} ({ox:<6},{oy:<6})    ({rx:<8.1f},{ry:<8.1f})")

# Show step-by-step for first vertex
print(f"\n--- Step-by-Step Calculation for {vert_labels[0]} ---")
print(format_vertex_calc(verts[0][0], verts[0][1], cx, cy, cos_a, sin_a))
print(f"\n{'=' * 60}")

# ---------------------------------------------------------------
# FIGURE SETUP — full-screen
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(22, 9))
plt.subplots_adjust(left=0.03, right=0.52, bottom=0.16, top=0.96)

# Maximize window (cross-backend)
mng = plt.get_current_fig_manager()
try:
    mng.window.state("zoomed")
except AttributeError:
    try:
        mng.window.showMaximized()
    except AttributeError:
        pass

flat = []
for v in verts:
    flat.extend(v)
for r in rotated:
    flat.extend(r)
flat.extend([cx, cy])
max_c = max(max(flat), -min(flat))
margin = max_c * 0.25 + 20
ax.set_xlim(-max_c - margin * 1.4, max_c + margin * 1.4)
ax.set_ylim(-max_c - margin * 0.8, max_c + margin * 0.8)
ax.set_aspect("equal")
ax.grid(True, alpha=0.12, color="#8888bb")
ax.axhline(0, color="#666699", linewidth=0.8, alpha=0.25)
ax.axvline(0, color="#666699", linewidth=0.8, alpha=0.25)

ax.set_facecolor("#0f0f23")
fig.patch.set_facecolor("#0f0f23")
ax.set_title(f"2D Rotation — {shape_name} about {rot_pt_name} ({dir_name}, {abs(angle)}\u00b0)",
             color="white", fontsize=16, fontweight="bold", pad=18)
ax.set_xlabel("X", color="white", fontsize=12, fontweight="bold")
ax.set_ylabel("Y", color="white", fontsize=12, fontweight="bold")
ax.tick_params(colors="white", labelsize=9, grid_alpha=0.3)

# ---------------------------------------------------------------
# STATIC ELEMENTS
# ---------------------------------------------------------------
orig_poly = mpatches.Polygon(
    verts, fill=False, edgecolor="#00d2ff", linewidth=2.5, label="Original"
)
ax.add_patch(orig_poly)

xs_orig = [v[0] for v in verts]
ys_orig = [v[1] for v in verts]
ax.scatter(xs_orig, ys_orig, c="#00d2ff", s=90, zorder=6,
           edgecolors="#006688", linewidths=1.5)

ax.scatter([cx], [cy], c="#ff4757", s=250, zorder=7,
           marker="*", edgecolors="#8b0000", linewidths=2)
pivot_ox, pivot_oy = smart_offset(cx, cy, verts, 28, 0)
ax.annotate(f"Pivot ({cx}, {cy})", (cx, cy),
            xytext=(pivot_ox, pivot_oy), textcoords="offset points",
            color="#ff4757", fontsize=11, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3",
                      facecolor="#1a1a35", edgecolor="#ff4757", alpha=0.9))

for (ox, oy), lbl in zip(verts, vert_labels):
    ax.annotate(f"{lbl} ({ox},{oy})", (ox, oy),
                xytext=(20, 4), textcoords="offset points",
                color="#00d2ff", fontsize=10, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.15",
                          facecolor="#0f0f23", edgecolor="#00d2ff", alpha=0.7,
                          mutation_scale=0.8))

# Full circular trajectories
for (ox, oy) in verts:
    dx, dy = ox - cx, oy - cy
    r = math.hypot(dx, dy)
    if r > 1:
        circ = plt.Circle((cx, cy), r, fill=False,
                          linestyle=":", linewidth=1.2, color="#8888bb", alpha=0.15)
        ax.add_patch(circ)

# ---------------------------------------------------------------
# DYNAMIC ELEMENTS
# ---------------------------------------------------------------
rot_tri = mpatches.Polygon(
    rotated, fill=False, edgecolor="#ff6b6b", linewidth=3.5, label="Rotated"
)
ax.add_patch(rot_tri)

rot_dots = ax.scatter(
    [r[0] for r in rotated], [r[1] for r in rotated],
    c="#ff6b6b", s=90, zorder=6, edgecolors="#8b0000", linewidths=1.5
)

rot_labels = []
for (rx, ry), lbl in zip(rotated, [f"{l}'" for l in vert_labels]):
    lb = ax.annotate(
        f"{lbl} ({int(rx)},{int(ry)})", (rx, ry),
        xytext=(-20, 4), textcoords="offset points",
        color="#ff6b6b", fontsize=10, fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.15",
                  facecolor="#0f0f23", edgecolor="#ff6b6b", alpha=0.7,
                  mutation_scale=0.8)
    )
    rot_labels.append(lb)
    rot_labels.append(lb)

# Ghost intermediate positions (subtle)
ghost_tris = []
ghost_fracs = [0.30, 0.65]
for frac in ghost_fracs:
    ga = angle * frac
    gverts = [rotate_point(x, y, cx, cy, ga) for (x, y) in verts]
    alpha = 0.08 + 0.25 * frac
    tri = mpatches.Polygon(
        gverts, fill=False, edgecolor="#ff6b6b",
        linewidth=0.8, linestyle="--", alpha=alpha
    )
    ax.add_patch(tri)
    ghost_tris.append(tri)

# Connection arrows (subtle direction indicators)
arrows = []
for (ox, oy), (rx, ry) in zip(verts, rotated):
    if math.hypot(rx - ox, ry - oy) > 2:
        arr = FancyArrowPatch(
            (ox, oy), (rx, ry),
            arrowstyle="->,head_width=5,head_length=6",
            color="#ffd93d", linewidth=1.0, linestyle="--", alpha=0.35,
            connectionstyle="arc3,rad=0.0"
        )
        ax.add_patch(arr)
        arrows.append(arr)

# Angle arc
angle_arc_r = min(max_c * 0.18, 25)
if angle_arc_r < 2:
    angle_arc_r = 10
arc_pts = get_arc_points(cx + angle_arc_r, cy, cx, cy, angle)
angle_arc_line, = ax.plot(
    [p[0] for p in arc_pts], [p[1] for p in arc_pts],
    color="#ffd93d", linewidth=2.5, alpha=0.85, zorder=4
)

mid_angle = angle / 2
mid_r = math.radians(mid_angle)
alr = angle_arc_r * 1.3
angle_label = ax.text(
    cx + alr * math.cos(mid_r), cy + alr * math.sin(mid_r),
    f"{abs(angle):.1f}\u00b0", color="#ffd93d",
    fontsize=12, fontweight="bold", ha="center", va="center",
    bbox=dict(boxstyle="round,pad=0.15",
              facecolor="#0f0f23", edgecolor="#ffd93d", alpha=0.85)
)

# Direction arrow at pivot
dir_len = angle_arc_r * 0.6
if angle > 0:
    dir_end = (cx + dir_len, cy)
    dir_angle = 0
else:
    dir_end = (cx - dir_len, cy)
    dir_angle = 180
dir_arrow = FancyArrowPatch(
    (cx, cy), dir_end,
    arrowstyle="->,head_width=6,head_length=8",
    color="#ffd93d", linewidth=2, alpha=0.6
)
ax.add_patch(dir_arrow)

# Arc path segments
arc_seg_lines = []
for (ox, oy) in verts:
    pts = get_arc_points(ox, oy, cx, cy, angle)
    ln, = ax.plot([p[0] for p in pts], [p[1] for p in pts],
                  color="#ffd93d", linewidth=1.5, alpha=0.3)
    arc_seg_lines.append(ln)

# Info box (right panel)
info_box = fig.text(
    0.56, 0.92, "",
    fontsize=11, verticalalignment="top", color="white",
    fontfamily="monospace",
    bbox=dict(boxstyle="round,pad=0.5",
              facecolor="#1a1a35", edgecolor="#8888bb", alpha=0.92)
)

# Formula box — shows step-by-step for first vertex (right panel)
formula_box = fig.text(
    0.56, 0.48, "",
    fontsize=9, verticalalignment="top", color="#00d2ff",
    fontfamily="monospace",
    bbox=dict(boxstyle="round,pad=0.4",
              facecolor="#0a0a1e", edgecolor="#00d2ff", alpha=0.85)
)

# Matrix box (right panel)
matrix_box = fig.text(
    0.56, 0.06, "",
    fontsize=10, verticalalignment="bottom", color="white",
    fontfamily="monospace",
    bbox=dict(boxstyle="round,pad=0.5",
              facecolor="#1a1a35", edgecolor="#8888bb", alpha=0.92)
)

legend = ax.legend(
    fontsize=10, loc="upper left",
    facecolor="#1a1a35", edgecolor="#8888bb", labelcolor="white"
)


def build_info(a):
    r = math.radians(a)
    cv, sv = math.cos(r), math.sin(r)
    d = dir_name if a >= 0 else "Clockwise"
    return (
        f"Shape: {shape_name}\n"
        f"Direction: {d}\n"
        f"Angle: {abs(a):.1f}\u00b0\n"
        f"Pivot: ({cx}, {cy})\n"
        f"cos\u03b8 = {cv:.4f}\n"
        f"sin\u03b8 = {sv:.4f}"
    ), (
        f"R(\u03b8) = [cos\u03b8  -sin\u03b8]\n"
        f"         [sin\u03b8   cos\u03b8]\n\n"
        f"       = [{cv:.4f}  {-sv:.4f}]\n"
        f"         [{sv:.4f}   {cv:.4f}]"
    ), format_vertex_calc(verts[0][0], verts[0][1], cx, cy,
                          math.cos(math.radians(a)), math.sin(math.radians(a)))


info_str, matrix_str, formula_str = build_info(angle)
info_box.set_text(info_str)
matrix_box.set_text(matrix_str)
formula_box.set_text(formula_str)

# ---------------------------------------------------------------
# SLIDER
# ---------------------------------------------------------------
ax_slider = plt.axes([0.15, 0.055, 0.70, 0.04])
slider = Slider(
    ax=ax_slider, label="Angle (\u00b0)", valmin=-360, valmax=360,
    valinit=angle, valstep=0.5,
    color="#ff6b6b", track_color="#3a3a5e"
)
slider.label.set_color("white")
slider.label.set_fontsize(12)
slider.valtext.set_color("white")
slider.valtext.set_fontsize(11)

# Direction label under slider
ax_dir_label = plt.axes([0.15, 0.022, 0.70, 0.025])
ax_dir_label.set_facecolor("#0f0f23")
ax_dir_label.set_xlim(0, 1)
ax_dir_label.set_ylim(0, 1)
ax_dir_label.axis("off")
dir_text = ax_dir_label.text(
    0.5, 0.5,
    "\u2190 Clockwise (-)                                   Anticlockwise (+) \u2192",
    color="#8888bb", fontsize=9, ha="center", va="center"
)


def update_plot(val):
    a = slider.val

    nrot = [rotate_point(x, y, cx, cy, a) for (x, y) in verts]

    rot_tri.set_xy(nrot)
    rot_dots.set_offsets(nrot)

    for lb, (rx, ry), lbl in zip(rot_labels, nrot,
                                  [f"{l}'" for l in vert_labels]):
        lb.set_position((rx, ry))
        lb.set_text(f"{lbl} ({int(rx)},{int(ry)})")
        lb.set_xytext((-20, 4))

    for tri, frac in zip(ghost_tris, ghost_fracs):
        ga = a * frac
        gverts = [rotate_point(x, y, cx, cy, ga) for (x, y) in verts]
        tri.set_xy(gverts)
        tri.set_alpha(0.08 + 0.25 * frac)

    for arr, (ox, oy), (rx, ry) in zip(arrows, verts, nrot):
        if math.hypot(rx - ox, ry - oy) > 2:
            arr.set_positions((ox, oy), (rx, ry))
            arr.set_visible(True)
        else:
            arr.set_visible(False)

    new_arc = get_arc_points(cx + angle_arc_r, cy, cx, cy, a)
    angle_arc_line.set_data([p[0] for p in new_arc], [p[1] for p in new_arc])

    mid_a = a / 2
    mid_r = math.radians(mid_a)
    angle_label.set_position((cx + alr * math.cos(mid_r),
                               cy + alr * math.sin(mid_r)))
    angle_label.set_text(f"{abs(a):.1f}\u00b0")

    # Direction arrow
    if a >= 0:
        dir_arrow.set_positions((cx, cy), (cx + dir_len, cy))
    else:
        dir_arrow.set_positions((cx, cy), (cx - dir_len, cy))

    for ln, (ox, oy) in zip(arc_seg_lines, verts):
        pts = get_arc_points(ox, oy, cx, cy, a)
        ln.set_data([p[0] for p in pts], [p[1] for p in pts])

    info_s, matrix_s, formula_s = build_info(a)
    info_box.set_text(info_s)
    matrix_box.set_text(matrix_s)
    formula_box.set_text(formula_s)

    fig.canvas.draw_idle()


slider.on_changed(update_plot)

# ---------------------------------------------------------------
# ANIMATE BUTTON
# ---------------------------------------------------------------
ax_btn = plt.axes([0.38, 0.105, 0.14, 0.04])
anim_btn = Button(ax_btn, "\u25b6 Animate", color="#3a3a5e", hovercolor="#5a5a7e")
anim_btn.label.set_color("white")
anim_btn.label.set_fontsize(11)
anim_btn.label.set_fontweight("bold")

_anim_running = False


def animate(event):
    global _anim_running
    if _anim_running:
        return
    _anim_running = True
    anim_btn.label.set_text("\u27f3 Animating...")
    fig.canvas.draw_idle()

    cur = slider.val
    step = 1.5
    if cur > 0:
        vals = [i * step for i in range(0, int(cur / step) + 1)]
    else:
        vals = [i * step for i in range(0, int(cur / step) - 1, -1)]
    for av in vals:
        slider.set_val(av)
        plt.pause(0.006)

    anim_btn.label.set_text("\u25b6 Animate")
    fig.canvas.draw_idle()
    _anim_running = False


anim_btn.on_clicked(animate)

# ---------------------------------------------------------------
# RESET BUTTON
# ---------------------------------------------------------------
ax_res = plt.axes([0.54, 0.105, 0.10, 0.04])
rst_btn = Button(ax_res, "\u21ba Reset", color="#3a3a5e", hovercolor="#5a5a7e")
rst_btn.label.set_color("white")
rst_btn.label.set_fontsize(10)

rst_btn.on_clicked(lambda e: slider.set_val(0))

# ---------------------------------------------------------------
# SHOW
# ---------------------------------------------------------------
plt.show()
