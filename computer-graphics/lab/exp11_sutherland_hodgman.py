import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

XMIN, YMIN = 150, 100
XMAX, YMAX = 450, 300

EDGE_NAMES = ["LEFT (x >= XMIN)", "RIGHT (x <= XMAX)", "TOP (y >= YMIN)", "BOTTOM (y <= YMAX)"]

def inside(p, edge):
    x, y = p
    if edge == 0:
        return x >= XMIN
    if edge == 1:
        return x <= XMAX
    if edge == 2:
        return y >= YMIN
    if edge == 3:
        return y <= YMAX
    return False

def intersect(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2
    if x2 != x1:
        m = (y2 - y1) / (x2 - x1)
    else:
        m = 1e10
    if edge == 0:
        return (XMIN, round(y1 + m * (XMIN - x1)))
    if edge == 1:
        return (XMAX, round(y1 + m * (XMAX - x1)))
    if edge == 2:
        x = round(x1 + (YMIN - y1) / m) if x2 != x1 else x1
        return (x, YMIN)
    if edge == 3:
        x = round(x1 + (YMAX - y1) / m) if x2 != x1 else x1
        return (x, YMAX)
    return (0, 0)

def clip_against_edge(poly, edge):
    if not poly:
        return []
    result = []
    n = len(poly)
    for i in range(n):
        curr = poly[i]
        nxt = poly[(i + 1) % n]
        curr_inside = inside(curr, edge)
        nxt_inside = inside(nxt, edge)

        if curr_inside and nxt_inside:
            result.append(nxt)
        elif curr_inside and not nxt_inside:
            result.append(intersect(curr, nxt, edge))
        elif not curr_inside and nxt_inside:
            result.append(intersect(curr, nxt, edge))
            result.append(nxt)
    return result

def draw_polygon(ax, poly, color, linewidth=2, label=None):
    if len(poly) < 3:
        return
    xs, ys = zip(*(poly + [poly[0]]))
    ax.plot(xs, ys, color=color, linewidth=linewidth, label=label)

print("=== Sutherland-Hodgman Polygon Clipping ===")
print(f"Clipping window: ({XMIN},{YMIN}) to ({XMAX},{YMAX})")
print("Enter polygon vertices (enter 'done' when finished):")

polygon = []
while True:
    inp = input("  x y (or 'done'): ").strip()
    if inp.lower() == "done":
        break
    try:
        px, py = map(int, inp.split())
        polygon.append((px, py))
    except:
        print("  Invalid. Enter: x y")

if len(polygon) < 3:
    print("Need at least 3 vertices!")
    exit()

print(f"\nOriginal polygon ({len(polygon)} vertices):")
for i, (px, py) in enumerate(polygon):
    print(f"  V{i}: ({px}, {py})")

print(f"\n{'Edge':<28} {'Vertices before':<6} {'Vertices after':<6}")
print("-" * 60)
clipped = polygon[:]
for edge in range(4):
    before = len(clipped)
    clipped = clip_against_edge(clipped, edge)
    print(f"{EDGE_NAMES[edge]:<28} {before:<16} {len(clipped):<14}")

print(f"\nClipped polygon ({len(clipped)} vertices):")
for i, (px, py) in enumerate(clipped):
    print(f"  V{i}: ({px}, {py})")

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Sutherland-Hodgman Polygon Clipping", color="white", fontsize=13)
ax.axhline(0, color="gray", linewidth=0.8, alpha=0.3)
ax.axvline(0, color="gray", linewidth=0.8, alpha=0.3)

all_x = [p[0] for p in polygon] + ([p[0] for p in clipped] if clipped else [])
all_y = [p[1] for p in polygon] + ([p[1] for p in clipped] if clipped else [])
margin = 30
ax.set_xlim(min(all_x + [XMIN]) - margin, max(all_x + [XMAX]) + margin)
ax.set_ylim(min(all_y + [YMIN]) - margin, max(all_y + [YMAX]) + margin)
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)

win = mpatches.Rectangle(
    (XMIN, YMIN), XMAX - XMIN, YMAX - YMIN,
    fill=True, facecolor="white", alpha=0.08,
    edgecolor="white", linewidth=2, label="Clipping Window"
)
ax.add_patch(win)

draw_polygon(ax, polygon, "white", 1.5, "Original polygon")

if clipped:
    draw_polygon(ax, clipped, "yellow", 2.5, "Clipped polygon")
    cx = sum(p[0] for p in clipped) // len(clipped)
    cy = sum(p[1] for p in clipped) // len(clipped)
    ax.text(cx - 15, cy, "CLIPPED", color="yellow", fontsize=9, fontweight="bold",
            bbox=dict(boxstyle="round", facecolor="#2b2b2b", alpha=0.7, edgecolor="yellow"))

for i, (px, py) in enumerate(polygon):
    ax.annotate(f"V{i}({px},{py})", (px, py), xytext=(5, 5),
                textcoords="offset points", color="white", fontsize=8)
if clipped:
    for i, (px, py) in enumerate(clipped):
        ax.scatter(px, py, c="yellow", s=40, zorder=4)

info = (
    f"Window: ({XMIN},{YMIN})-({XMAX},{YMAX})\n"
    f"Original: {len(polygon)} vertices\n"
    f"Clipped: {len(clipped)} vertices"
)
ax.text(0.02, 0.98, info, transform=ax.transAxes,
        fontsize=9, verticalalignment="top", color="black",
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
