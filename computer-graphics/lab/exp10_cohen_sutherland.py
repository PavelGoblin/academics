import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

XMIN, YMIN = 150, 100
XMAX, YMAX = 450, 300

def compute_code(x, y):
    code = INSIDE
    if x < XMIN:
        code |= LEFT
    elif x > XMAX:
        code |= RIGHT
    if y < YMIN:
        code |= TOP
    elif y > YMAX:
        code |= BOTTOM
    return code

def code_to_str(code):
    parts = []
    if code == 0:
        return "INSIDE"
    if code & LEFT:
        parts.append("LEFT")
    if code & RIGHT:
        parts.append("RIGHT")
    if code & TOP:
        parts.append("TOP")
    if code & BOTTOM:
        parts.append("BOTTOM")
    return "|".join(parts)

def cohen_sutherland_clip(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False
    steps = []

    while True:
        steps.append((x1, y1, x2, y2, code1, code2, "accept" if accept else "processing"))

        if code1 == 0 and code2 == 0:
            accept = True
            steps.append((x1, y1, x2, y2, code1, code2, "ACCEPTED"))
            break
        elif code1 & code2:
            steps.append((x1, y1, x2, y2, code1, code2, "REJECTED (trivial)"))
            break
        else:
            code_out = code1 if code1 != 0 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (YMIN - y1) / (y2 - y1)
                y = YMIN
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (YMAX - y1) / (y2 - y1)
                y = YMAX
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (XMAX - x1) / (x2 - x1)
                x = XMAX
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (XMIN - x1) / (x2 - x1)
                x = XMIN

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        return (round(x1), round(y1), round(x2), round(y2)), steps
    return None, steps

print("=== Cohen-Sutherland Line Clipping ===")
print(f"Clipping window: ({XMIN},{YMIN}) to ({XMAX},{YMAX})")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

code1_init = compute_code(x1, y1)
code2_init = compute_code(x2, y2)

print(f"\nInitial region codes:")
print(f"  P1({x1},{y1}) -> {code_to_str(code1_init)} (binary: {code1_init:04b})")
print(f"  P2({x2},{y2}) -> {code_to_str(code2_init)} (binary: {code2_init:04b})")

clipped, steps = cohen_sutherland_clip(x1, y1, x2, y2)

print(f"\n{'Step':<6} {'x1':<6} {'y1':<6} {'x2':<6} {'y2':<6} {'code1':<16} {'code2':<16} {'Status':<20}")
print("-" * 92)
for i, (sx1, sy1, sx2, sy2, c1, c2, status) in enumerate(steps):
    print(f"{i:<6} {sx1:<6} {sy1:<6} {sx2:<6} {sy2:<6} "
          f"{code_to_str(c1):<16} {code_to_str(c2):<16} {status:<20}")

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Cohen-Sutherland Line Clipping", color="white", fontsize=13)

ax.axhline(0, color="gray", linewidth=0.8, alpha=0.3)
ax.axvline(0, color="gray", linewidth=0.8, alpha=0.3)

margin = 30
ax.set_xlim(min(x1, x2, XMIN) - margin, max(x1, x2, XMAX) + margin)
ax.set_ylim(min(y1, y2, YMIN) - margin, max(y1, y2, YMAX) + margin)
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)

win = mpatches.Rectangle(
    (XMIN, YMIN), XMAX - XMIN, YMAX - YMIN,
    fill=True, facecolor="white", alpha=0.08,
    edgecolor="white", linewidth=2, label="Clipping Window"
)
ax.add_patch(win)
ax.text((XMIN + XMAX) // 2 - 40, YMIN - 18, "Clipping Window",
        color="white", fontsize=8, fontweight="bold", alpha=0.7)

ax.plot([x1, x2], [y1, y2], "w-", linewidth=1.5, alpha=0.5, label="Original line")
ax.scatter([x1, x2], [y1, y2], c="white", s=60, zorder=4)

if clipped:
    cx1, cy1, cx2, cy2 = clipped
    ax.plot([cx1, cx2], [cy1, cy2], "y-", linewidth=3, label="Clipped (visible)")
    ax.scatter([cx1, cx2], [cy1, cy2], c="yellow", s=80, zorder=5, edgecolors="darkgoldenrod")
    ax.annotate(f"({cx1},{cy1})", (cx1, cy1), xytext=(5, 5),
                textcoords="offset points", color="yellow", fontsize=9, fontweight="bold")
    ax.annotate(f"({cx2},{cy2})", (cx2, cy2), xytext=(5, 5),
                textcoords="offset points", color="yellow", fontsize=9, fontweight="bold")
    result_text = "Line: PARTIALLY / FULLY VISIBLE"
else:
    result_text = "Line: REJECTED (outside window)"

ax.annotate(f"P1({x1},{y1})", (x1, y1), xytext=(5, 5),
            textcoords="offset points", color="white", fontsize=9)
ax.annotate(f"P2({x2},{y2})", (x2, y2), xytext=(5, 5),
            textcoords="offset points", color="white", fontsize=9)

info = (
    f"Window: ({XMIN},{YMIN})-({XMAX},{YMAX})\n"
    f"P1 code: {code_to_str(code1_init)} ({code1_init:04b})\n"
    f"P2 code: {code_to_str(code2_init)} ({code2_init:04b})\n"
    f"Result: {result_text}"
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
