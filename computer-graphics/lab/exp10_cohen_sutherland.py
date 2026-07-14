"""
Lab 8: Line Clipping using Cohen-Sutherland (Interactive)
=========================================================
Computer Graphics Course

Clips line segments against a rectangular window using the
Cohen-Sutherland algorithm, then plots them in a centered 4-axis
(x / x' , y / y') coordinate view so original and clipped endpoints
can be compared directly.

The clip window is defined by two inputs:
    BL = Bottom-Left  (xmin, ymin)
    UR = Upper-Right  (xmax, ymax)

Outcode bits (relative to the window xmin,ymin,xmax,ymax):
    1000 TOP, 0100 BOTTOM, 0010 RIGHT, 0001 LEFT

Algorithm
---------
1. Compute outcodes for both endpoints.
2. Both 0000  -> ACCEPT (trivially inside).
3. Shared bit  -> REJECT (completely outside a region).
4. Else clip the outside endpoint at a boundary and repeat.

Requirements:
    pip install matplotlib numpy
"""

import numpy as np
import matplotlib.pyplot as plt

INSIDE = 0b0000
LEFT = 0b0001
RIGHT = 0b0010
BOTTOM = 0b0100
TOP = 0b1000


def compute_outcode(x, y, win):
    xmin, ymin, xmax, ymax = win
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code


def clip_line(x0, y0, x1, y1, win):
    """Clip segment against the window. Returns (accepted, (x0,y0),(x1,y1))."""
    xmin, ymin, xmax, ymax = win
    code0 = compute_outcode(x0, y0, win)
    code1 = compute_outcode(x1, y1, win)
    accepted = False

    while True:
        if code0 == 0 and code1 == 0:
            accepted = True
            break
        elif code0 & code1:
            break
        else:
            code_out = code0 if code0 != 0 else code1
            if code_out & TOP:
                x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
                y = ymax
            elif code_out & BOTTOM:
                x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
                y = ymin
            elif code_out & RIGHT:
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
                x = xmax
            elif code_out & LEFT:
                y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
                x = xmin

            if code_out == code0:
                x0, y0 = x, y
                code0 = compute_outcode(x0, y0, win)
            else:
                x1, y1 = x, y
                code1 = compute_outcode(x1, y1, win)

    if accepted:
        return True, (x0, y0), (x1, y1)
    return False, (None, None), (None, None)


def plot_4axis(lines, win):
    xmin, ymin, xmax, ymax = win
    fig, ax = plt.subplots(figsize=(8, 8))

    # clipping window
    rect = plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                         fill=False, edgecolor='k', linewidth=2,
                         label='Clip window (BL-UR)')
    ax.add_patch(rect)

    all_pts = []
    for (x0, y0, x1, y1) in lines:
        all_pts.extend([(x0, y0), (x1, y1)])
        ax.plot([x0, x1], [y0, y1], 'b--', alpha=0.6,
                label='Original' if (x0, y0, x1, y1) == lines[0] else "")
        accepted, p0, p1 = clip_line(x0, y0, x1, y1, win)
        if accepted:
            all_pts.extend([p0, p1])
            ax.plot([p0[0], p1[0]], [p0[1], p1[1]], 'r-', linewidth=2.5,
                    label='Clipped (x\',y\')' if (x0, y0, x1, y1) == lines[0] else "")
            ax.plot([x0, p0[0]], [y0, p0[1]], 'g:', alpha=0.5)
            ax.plot([x1, p1[0]], [y1, p1[1]], 'g:', alpha=0.5)

    if all_pts:
        lim = np.max(np.abs(np.array(all_pts))) * 1.2 + 1.0
    else:
        lim = 15.0

    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect('equal')
    ax.axhline(0, color='k', linewidth=1.2)
    ax.axvline(0, color='k', linewidth=1.2)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlabel("x  /  x'  (horizontal)")
    ax.set_ylabel("y  /  y'  (vertical)")
    ax.set_title("Cohen-Sutherland Line Clipping [4-axis view]")
    ax.legend()
    plt.tight_layout()
    plt.savefig("clipping_graph.png", dpi=120)
    print("Graph saved to clipping_graph.png")
    plt.show()


def main():
    print("=== Cohen-Sutherland Line Clipping (interactive) ===")

    print("Define clip window:")
    blx = float(input("  BL x (bottom-left): "))
    bly = float(input("  BL y (bottom-left): "))
    urx = float(input("  UR x (upper-right): "))
    ury = float(input("  UR y (upper-right): "))
    win = (blx, bly, urx, ury)
    print(f"Clip window: x[{blx},{urx}]  y[{bly},{ury}]")

    n = int(input("Enter number of lines: "))
    lines = []
    for i in range(n):
        print(f"  Line {i+1} (x0 y0 x1 y1):")
        x0 = float(input("    x0: "))
        y0 = float(input("    y0: "))
        x1 = float(input("    x1: "))
        y1 = float(input("    y1: "))
        lines.append((x0, y0, x1, y1))

    print("\n--- Results ---")
    for (x0, y0, x1, y1) in lines:
        accepted, p0, p1 = clip_line(x0, y0, x1, y1, win)
        if accepted:
            print(f"Line ({x0},{y0})-({x1},{y1}): ACCEPTED -> "
                  f"({p0[0]:.2f},{p0[1]:.2f}) to ({p1[0]:.2f},{p1[1]:.2f})")
        else:
            print(f"Line ({x0},{y0})-({x1},{y1}): REJECTED")

    plot_4axis(lines, win)


if __name__ == "__main__":
    main()
