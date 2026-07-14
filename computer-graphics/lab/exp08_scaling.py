"""
Lab 7: N-Dimensional Scaling Transformation (Interactive)
=========================================================
Computer Graphics Course

This lab demonstrates the SCALE transformation in N dimensions using
homogeneous (4-axis) coordinates and a 4x4 transformation matrix.

Theory
------
    x'_i = s_i * x_i      for i in 0..n-1

In homogeneous 4-axis coordinates every point is stored as a 4-vector:

    [ x0, x1, ..., 0, 1 ]

so the result is always expressed in 4 axes regardless of the chosen
dimension n (2D or 3D, ...). The scaling matrix is a 4x4 matrix with the
n scale factors on the leading diagonal and 1 elsewhere:

        [ s0  0   0   0 ]
        [ 0   s1  0   0 ]
    T = [ 0   0  s2  0 ]
        [ 0   0   0   1 ]

    [x'0 x'1 x'2 x'3] = [x0 x1 x2 x3] * T

The number of vertices defines the shape:
    2 vertices -> straight line
    3 vertices -> triangle
    4 vertices -> rectangle

The graph shows a 4-axis centered coordinate system (x / x' and y / y')
so you can compare the original and scaled shapes.

Requirements:
    pip install matplotlib numpy
"""

import numpy as np
import matplotlib.pyplot as plt


def scale_matrix_4(sf):
    """Build a 4x4 scaling matrix from a list of n scale factors."""
    T = np.eye(4)
    for i, s in enumerate(sf):
        T[i, i] = s
    return T


def scale_points(points, sf):
    """
    Scale `points` (list of n-dim vertices) about the origin.

    Returns the homogeneous 4-vector forms of the original and scaled
    points (each padded to 4 axes).
    """
    dim = len(sf)
    hom = []
    for p in points:
        v = list(p) + [0.0] * (4 - dim - 1) + [1.0]
        hom.append(v)
    hom = np.array(hom)
    T = scale_matrix_4(sf)
    scaled = hom @ T
    return hom, scaled


def plot_4axis(original_hom, scaled_hom, sf):
    """Plot original and transformed shapes in a centered 4-axis view."""
    fig, ax = plt.subplots(figsize=(8, 8))

    o2 = original_hom[:, :2]
    s2 = scaled_hom[:, :2]
    all_pts = np.vstack([o2, s2])
    lim = np.max(np.abs(all_pts)) * 1.2 + 1.0
    lim = float(lim)

    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect('equal')

    # 4-axis centered grid
    ax.axhline(0, color='k', linewidth=1.2)
    ax.axvline(0, color='k', linewidth=1.2)
    ax.grid(True, linestyle='--', alpha=0.5)

    ax.set_xlabel("x0 / x0' (horizontal)")
    ax.set_ylabel("x1 / x1' (vertical)")
    factors = ", ".join(f"s{i+1}={s}" for i, s in enumerate(sf))
    ax.set_title(f"Scaling: original vs scaled  [4-axis view, {factors}]")

    # original shape
    poly = np.vstack([o2, o2[0]])
    ax.plot(poly[:, 0], poly[:, 1], 'b-o', label='Original (x, y)')

    # scaled shape
    poly_s = np.vstack([s2, s2[0]])
    ax.plot(poly_s[:, 0], poly_s[:, 1], 'r-o', label='Scaled (x\', y\')')

    # connectors from original to scaled vertices
    for (ox, oy), (sx_, sy_) in zip(o2, s2):
        ax.plot([ox, sx_], [oy, sy_], 'g:', alpha=0.6)

    ax.legend()
    plt.tight_layout()
    plt.savefig("scaling_graph.png", dpi=120)
    print("Graph saved to scaling_graph.png")
    plt.show()


def main():
    print("=== N-D Scaling Lab (interactive) ===")

    n = int(input("Enter dimension n (e.g. 2 or 3): "))
    m = int(input("Enter number of vertices (2=line, 3=triangle, 4=rectangle): "))

    pts = []
    for i in range(m):
        coords = []
        for d in range(n):
            coords.append(float(input(f"  Vertex {i+1} coordinate {d+1}: ")))
        pts.append(coords)
    original = np.array(pts)

    sf = []
    for d in range(n):
        sf.append(float(input(f"Enter scale factor s{d+1}: ")))

    original_hom, scaled = scale_points(pts, sf)

    print("\n--- Results (always in 4 axes) ---")
    print("Original (4-axis):")
    for v in original_hom:
        print("  " + "  ".join(f"{c:8.4f}" for c in v))
    print("Scaled  (4-axis):")
    for v in scaled:
        print("  " + "  ".join(f"{c:8.4f}" for c in v))

    plot_4axis(original_hom, scaled, sf)


if __name__ == "__main__":
    main()
