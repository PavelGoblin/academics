"""
Lab 9: Bézier Curves (Interactive)
====================================
Computer Graphics Course

Bézier curves are parametric curves widely used in computer graphics
and CAD. A Bézier curve of degree n is defined by n+1 control points:

    B(t) = sum_{i=0}^{n} P_i * B_i^n(t)    t in [0, 1]

where B_i^n(t) are the Bernstein basis polynomials:

    B_i^n(t) = C(n, i) * t^i * (1-t)^{n-i}

Implementation
--------------
Two equivalent evaluation methods are provided:
  1. Bernstein (algebraic)  — uses the formula above.
  2. De Casteljau (geometric) — recursive linear interpolation;
     more numerically stable.

This demo lets the user enter 2D control points interactively, then
draws the control polygon and the smooth Bézier curve on a 4-axis
centered graph.  The Bernstein basis functions are also plotted in a
separate figure.

Requirements:
    pip install matplotlib numpy
"""

import numpy as np
import matplotlib.pyplot as plt
from math import comb


def bernstein_basis(i, n, t):
    """Evaluate the i-th Bernstein basis polynomial of degree n at t."""
    return comb(n, i) * (t ** i) * ((1 - t) ** (n - i))


def bezier_bernstein(ctrl, num=200):
    """
    Evaluate a Bézier curve using the Bernstein (algebraic) form.

    Parameters
    ----------
    ctrl : ndarray, shape (n+1, 2)
        Control points.
    num  : int
        Number of sample points on the curve.

    Returns
    -------
    curve : ndarray, shape (num, 2)
        Points on the Bézier curve.
    """
    n = len(ctrl) - 1
    t = np.linspace(0, 1, num)
    curve = np.zeros((num, 2))
    for i, p in enumerate(ctrl):
        basis = bernstein_basis(i, n, t)
        curve[:, 0] += basis * p[0]
        curve[:, 1] += basis * p[1]
    return curve


def de_casteljau(ctrl, t):
    """
    Evaluate a Bézier curve at a single t using De Casteljau's algorithm.

    Parameters
    ----------
    ctrl : ndarray, shape (n+1, 2)
        Control points.
    t    : float
        Parameter value in [0, 1].

    Returns
    -------
    point : ndarray, shape (2,)
        Point on the curve at parameter t.
    """
    pts = np.array(ctrl, dtype=float)
    while len(pts) > 1:
        pts = np.array([(1 - t) * pts[j] + t * pts[j + 1] for j in range(len(pts) - 1)])
    return pts[0]


def bezier_casteljau(ctrl, num=200):
    """
    Evaluate a Bézier curve using De Casteljau's algorithm.

    Returns
    -------
    curve : ndarray, shape (num, 2)
    """
    t_vals = np.linspace(0, 1, num)
    return np.array([de_casteljau(ctrl, t) for t in t_vals])


def plot_bezier(ctrl, steps=300, method="casteljau"):
    ctrl = np.array(ctrl, dtype=float)
    curve = bezier_casteljau(ctrl, steps) if method == "casteljau" else bezier_bernstein(ctrl, steps)

    all_pts = np.vstack([ctrl, curve])
    lim = np.max(np.abs(all_pts)) * 1.2 + 0.5
    lim = float(lim)

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect('equal')
    ax.axhline(0, color='k', linewidth=1.2)
    ax.axvline(0, color='k', linewidth=1.2)
    ax.grid(True, linestyle='--', alpha=0.5)

    # Control polygon (dashed grey)
    ax.plot(ctrl[:, 0], ctrl[:, 1], 'o-', color='#888888',
            linewidth=2, markersize=8, label='Control polygon')

    # Bézier curve (blue)
    ax.plot(curve[:, 0], curve[:, 1], 'b-', linewidth=2.5,
            label=f'Bézier curve (De Casteljau)' if method == 'casteljau'
                  else 'Bézier curve (Bernstein)')

    # Label control points
    for i, (x, y) in enumerate(ctrl):
        ax.annotate(f"P{i}", (x, y), textcoords="offset points",
                    xytext=(8, 8), fontsize=10, fontweight='bold',
                    color='#333333')

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"Bézier Curve — {len(ctrl)} control points (degree {len(ctrl)-1})")
    ax.legend()
    plt.tight_layout()
    plt.savefig("bezier_graph.png", dpi=120)
    print("Graph saved to bezier_graph.png")
    plt.show()


def plot_basis_functions(n, steps=300):
    t = np.linspace(0, 1, steps)
    fig, ax = plt.subplots(figsize=(8, 5))
    for i in range(n + 1):
        b = bernstein_basis(i, n, t)
        ax.plot(t, b, lw=2, label=f"B_{i}^{n}(t)")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.1)
    ax.set_xlabel("t")
    ax.set_ylabel("B_i^n(t)")
    ax.set_title(f"Bernstein Basis Functions — Degree {n}")
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    plt.tight_layout()
    plt.savefig("bezier_basis.png", dpi=120)
    print("Basis graph saved to bezier_basis.png")
    plt.show()


def main():
    print("=== Bézier Curves Lab (Interactive) ===")
    print("Enter 2D control points for the Bézier curve.")
    print("The curve degree = number of points - 1.")

    m = int(input("Number of control points (>=2): "))
    steps = int(input("Number of steps (curve resolution, e.g. 100-500): "))

    ctrl = []
    for i in range(m):
        x = float(input(f"  P{i} x: "))
        y = float(input(f"  P{i} y: "))
        ctrl.append((x, y))

    ctrl_arr = np.array(ctrl)
    n = len(ctrl_arr) - 1

    print(f"\nDegree of Bézier curve: {n}")
    print(f"Control points: {ctrl}")
    print(f"Curve steps (resolution): {steps}")

    # Evaluate at a few sample t values using both methods
    print("\n--- Sample evaluations ---")
    print("   t    |  Bernstein (x,y)      | De Casteljau (x,y)")
    print("--------|------------------------|---------------------")
    for t_val in np.linspace(0, 1, 5):
        b_pt = bezier_bernstein(ctrl_arr, steps)
        idx = int(t_val * (steps - 1))
        bxy = b_pt[min(idx, steps - 1)]
        cxy = de_casteljau(ctrl_arr, t_val)
        print(f"  {t_val:.2f}  |  ({bxy[0]:8.4f}, {bxy[1]:8.4f})  |  ({cxy[0]:8.4f}, {cxy[1]:8.4f})")

    # Plot
    print("\nPlotting Bézier curve with control polygon...")
    plot_bezier(ctrl_arr, steps=steps, method="casteljau")

    show_basis = input(f"\nShow Bernstein basis functions for degree {n}? (y/n): ").strip().lower()
    if show_basis == 'y':
        plot_basis_functions(n, steps=steps)


if __name__ == "__main__":
    main()
