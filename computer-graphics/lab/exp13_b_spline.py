import matplotlib.pyplot as plt
import numpy as np

def b_spline_curve(control_x, control_y, steps=50):
    n = len(control_x)
    all_px, all_py = [], []

    print(f"\n{'Segment':<10} {'t':<8} {'B0(t)':<10} {'B1(t)':<10} {'B2(t)':<10} {'B3(t)':<10} {'X(t)':<10} {'Y(t)':<10}")
    print("-" * 78)

    for i in range(n - 3):
        ts = np.linspace(0, 1, steps + 1)
        t2 = ts ** 2
        t3 = ts ** 3

        b0 = (-t3 + 3*t2 - 3*ts + 1) / 6.0
        b1 = (3*t3 - 6*t2 + 4) / 6.0
        b2 = (-3*t3 + 3*t2 + 3*ts + 1) / 6.0
        b3 = t3 / 6.0

        px = (b0 * control_x[i] + b1 * control_x[i+1]
              + b2 * control_x[i+2] + b3 * control_x[i+3])
        py = (b0 * control_y[i] + b1 * control_y[i+1]
              + b2 * control_y[i+2] + b3 * control_y[i+3])

        all_px.extend(px)
        all_py.extend(py)

        for j in range(0, steps + 1, 10):
            t_val = j / steps
            print(f"Seg{i}:    {t_val:<8.2f} {b0[j]:<10.4f} {b1[j]:<10.4f} {b2[j]:<10.4f} {b3[j]:<10.4f} {px[j]:<10.2f} {py[j]:<10.2f}")

    return all_px, all_py

print("=== Uniform Cubic B-Spline ===")
print("Enter control points (enter 'done' when finished):")
ctrl_x, ctrl_y = [], []
while True:
    inp = input("  x y (or 'done'): ").strip()
    if inp.lower() == "done":
        break
    try:
        px, py = map(int, inp.split())
        ctrl_x.append(px)
        ctrl_y.append(py)
    except:
        print("  Invalid. Enter: x y")

if len(ctrl_x) < 4:
    print("Need at least 4 control points!")
    exit()

print(f"\nControl points ({len(ctrl_x)}):")
for i in range(len(ctrl_x)):
    print(f"  P{i}: ({ctrl_x[i]}, {ctrl_y[i]})")

px, py = b_spline_curve(ctrl_x, ctrl_y)

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Uniform Cubic B-Spline Curve", color="white", fontsize=13)
ax.axhline(0, color="gray", linewidth=0.8, alpha=0.3)
ax.axvline(0, color="gray", linewidth=0.8, alpha=0.3)

all_x = ctrl_x + [round(p) for p in px]
all_y = ctrl_y + [round(p) for p in py]
margin = 30
ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
ax.set_ylim(min(all_y) - margin, max(all_y) + margin)
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)

seg_colors = ["yellow", "lime", "cyan", "magenta", "orange", "pink"]
n_segments = len(ctrl_x) - 3
for i in range(n_segments):
    start = i * 51
    end = (i + 1) * 51
    if end <= len(px):
        ax.plot(px[start:end], py[start:end],
                color=seg_colors[i % len(seg_colors)], linewidth=2.5,
                label=f"Segment {i}" if i < 6 else None)

ax.plot(ctrl_x, ctrl_y, "w--", linewidth=1.5, label="Control polygon")
ax.scatter(ctrl_x, ctrl_y, c="red", s=80, zorder=5, edgecolors="white")
for i in range(len(ctrl_x)):
    ax.annotate(f"P{i}({ctrl_x[i]},{ctrl_y[i]})", (ctrl_x[i], ctrl_y[i]),
                xytext=(8, 8), textcoords="offset points",
                color="red", fontsize=9, fontweight="bold")

info = (
    f"Control points: {len(ctrl_x)}\n"
    f"Segments: {n_segments}\n"
    f"Uniform cubic B-spline\n"
    f"C² continuous (smooth)"
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
