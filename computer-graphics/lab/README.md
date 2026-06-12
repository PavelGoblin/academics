# Computer Graphics Lab

![Language](https://img.shields.io/badge/Language-C%2B%2B%20%7C%20Python-blue)
![Graphics](https://img.shields.io/badge/Graphics-Windows%20BGI%20%7C%20Matplotlib-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

> A comprehensive collection of 13 computer graphics experiments covering line drawing algorithms, 2D/3D transformations, clipping, and curve generation — implemented in both **C++ (BGI)** and **Python (Matplotlib)**.

**Part of [Academics](https://github.com/PavelGoblin/academics)** | [Live Preview](https://html-preview.github.io/?url=https://github.com/PavelGoblin/academics/blob/main/computer-graphics/lab/index.html)

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup & Installation](#setup--installation)
- [Quick Start](#quick-start)
- [Experiments](#experiments)
  - [Exp 01 — I/O Devices](#exp-01--io-devices-theory)
  - [Exp 02 — Slope-Intercept Line](#exp-02--slope-intercept-line-drawing)
  - [Exp 03 — DDA Line Algorithm](#exp-03--dda-line-algorithm)
  - [Exp 04 — Bresenham's Line Algorithm](#exp-04--bresenhams-line-algorithm)
  - [Exp 05 — Midpoint Circle Algorithm](#exp-05--midpoint-circle-algorithm)
  - [Exp 06 — 2D Translation](#exp-06--2d-translation)
  - [Exp 07 — 2D Rotation](#exp-07--2d-rotation)
  - [Exp 08 — 2D Scaling](#exp-08--2d-scaling)
  - [Exp 09 — 3D Rotation](#exp-09--3d-rotation-about-arbitrary-axis)
  - [Exp 10 — Cohen-Sutherland Clipping](#exp-10--cohen-sutherland-line-clipping)
  - [Exp 11 — Sutherland-Hodgman Clipping](#exp-11--sutherland-hodgman-polygon-clipping)
  - [Exp 12 — Bézier Curves](#exp-12--bezier-curves)
  - [Exp 13 — B-Spline Curves](#exp-13--b-spline-curves)
- [File Structure](#file-structure)
- [References](#references)

---

## Overview

Computer Graphics is the science of generating visual content using computers. This lab covers the foundational algorithms that form the backbone of all graphics rendering — from drawing a single pixel to clipping polygons and generating smooth curves.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    COMPUTER GRAPHICS PIPELINE                       │
│                                                                     │
│   ┌──────────┐   ┌──────────────┐   ┌───────────┐   ┌──────────┐  │
│   │  INPUT   │──▶│  GEOMETRY    │──▶│  CLIPPING  │──▶│ DISPLAY  │  │
│   │ (Points) │   │ (Transforms) │   │ (Culling)  │   │ (Pixels) │  │
│   └──────────┘   └──────────────┘   └───────────┘   └──────────┘  │
│                                                                     │
│   Exp 01        Exp 06-09           Exp 10-11       Exp 02-05,12-13│
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### What You'll Learn

| Category | Concepts |
|----------|----------|
| **Line Drawing** | Slope-Intercept, DDA, Bresenham's algorithms |
| **Circle Drawing** | Midpoint circle algorithm |
| **2D Transforms** | Translation, Rotation, Scaling |
| **3D Transforms** | Rotation about arbitrary axis (Rodrigues' formula) |
| **Clipping** | Cohen-Sutherland (line), Sutherland-Hodgman (polygon) |
| **Curve Generation** | Bézier curves, B-Spline curves |

---

## Prerequisites

### C++ (Windows BGI)

| Requirement | Purpose |
|-------------|---------|
| **MinGW-w64** (g++) | C++ compiler |
| **graphics.h** | Windows BGI graphics library |
| **winbgim.h** | BGI extension for Windows |
| **libbgi.a** | BGI static library |

### Python

| Requirement | Purpose |
|-------------|---------|
| **Python 3.8+** | Interpreter |
| **matplotlib** | Plotting and visualization |
| **numpy** | Numerical computations |

```bash
pip install matplotlib numpy
```

---

## Setup & Installation

### Automated Setup (PowerShell)

```powershell
# Clone the repository
git clone https://github.com/PavelGoblin/academics.git
cd academics/computer-graphics/lab

# Run the setup script (checks g++, copies headers)
.\setup.ps1

# Launch the interactive menu
.\menu.ps1
```

### Manual Setup

1. Ensure `g++` is in your PATH
2. Place `graphics.h`, `winbgim.h`, and `libbgi.a` in the `include/` directory
3. Compile any experiment manually:

```powershell
g++ -o exp02.exe exp02_slope_intercept.cpp -I include -L include \
    -static-libgcc -static-libstdc++ -lbgi -lgdi32 -lcomdlg32 -luuid -loleaut32 -lole32
```

---

## Quick Start

### Run C++ experiments

```powershell
# Using the menu
.\menu.ps1

# Direct run (experiment 2-13)
.\run.ps1 -Experiment 4
```

### Run Python experiments

```bash
# Any experiment (02-13)
python exp04_bresenham_line.py
python exp09_3d_rotation.py
```

### Render all experiments at once

```bash
python render_all.py
```

---

## Experiments

---

### Exp 01 — I/O Devices (Theory)

> **File:** `exp01_io_devices.md`

A theoretical study of input and output devices used in computer graphics.

#### Input Devices Overview

```
                    INPUT DEVICES
                         │
        ┌────────────────┼────────────────┐
        │                │                │
   ┌────▼────┐    ┌──────▼──────┐   ┌────▼─────┐
   │ Pointing│    │   Scanning  │   │  Audio/  │
   │ Devices │    │   Devices   │   │  Video   │
   └────┬────┘    └──────┬──────┘   └────┬─────┘
        │                │               │
   Mouse, Touchpad   Scanner, Camera  Microphone
   Joystick, Pen     Barcode Reader   Webcam
   Trackball, Tablet  Digitizer        VR Glove
```

#### Output Devices Classification

```
                     OUTPUT DEVICES
                          │
           ┌──────────────┼──────────────┐
           │              │              │
      ┌────▼────┐   ┌────▼────┐   ┌────▼────┐
      │ Visual  │   │  Print  │   │  Audio  │
      └────┬────┘   └────┬────┘   └────┬────┘
           │              │              │
      Monitor        Dot Matrix      Speakers
      Projector      Inkjet          Headphones
      Plotter        Laser           VR Headset
                     Thermal
                     3D Printer
```

#### Hardcopy vs Softcopy

| Aspect | Hardcopy | Softcopy |
|--------|----------|----------|
| Medium | Physical (paper) | Electronic (screen) |
| Permanent | Yes | No |
| Devices | Printer, Plotter | Monitor, Projector |

---

### Exp 02 — Slope-Intercept Line Drawing

> **Files:** `exp02_slope_intercept.cpp` | `exp02_slope_intercept.py`

#### Theory

The simplest line drawing algorithm uses the slope-intercept form of a line:

```
y = mx + c

where:
  m = slope = (y₂ - y₁) / (x₂ - x₁)
  c = y-intercept = y₁ - m·x₁
```

#### Algorithm

```
┌─────────────────────────────────────────────┐
│           SLOPE-INTERCEPT METHOD             │
├─────────────────────────────────────────────┤
│ Input: (x₁,y₁), (x₂,y₂)                   │
│                                             │
│ 1. Compute dx = x₂ - x₁                    │
│    Compute dy = y₂ - y₁                     │
│                                             │
│ 2. Compute m = dy/dx                        │
│    Compute c = y₁ - m·x₁                   │
│                                             │
│ 3. If |dx| ≥ |dy|:                          │
│      For each x from x₁ to x₂:             │
│        y = round(m·x + c)                   │
│        Plot pixel (x, y)                    │
│    Else:                                    │
│      For each y from y₁ to y₂:             │
│        x = round((y - c) / m)               │
│        Plot pixel (x, y)                    │
└─────────────────────────────────────────────┘
```

#### Limitation

- Uses **floating-point division** → slow
- Accumulated rounding errors for steep lines
- Not suitable for real-time rendering

---

### Exp 03 — DDA Line Algorithm

> **Files:** `exp03_dda_line.cpp` | `exp03_dda_line.py`

#### Theory

**DDA (Digital Differential Analyzer)** eliminates the slope-intercept equation by using incremental calculation.

```
DDA INCREMENTAL METHOD:

  dx = x₂ - x₁
  dy = y₂ - y₁
  steps = max(|dx|, |dy|)

  x_increment = dx / steps
  y_increment = dy / steps

  x, y = x₁, y₁
  for i = 0 to steps:
      plot(round(x), round(y))
      x += x_increment
      y += y_increment
```

#### Visual Explanation

```
  Start (100,100)          End (400,300)
       ●───────────────────────●
       │                       │
       │   dx = 300, dy = 200  │
       │   steps = 300         │
       │   x_inc = 1.0         │
       │   y_inc = 0.67        │
       │                       │
  Each step: x += 1.0, y += 0.67
  Round y to nearest integer for pixel
```

#### Comparison with Slope-Intercept

| Aspect | Slope-Intercept | DDA |
|--------|----------------|-----|
| Multiplications | Per pixel | None |
| Additions | 2 per pixel | 2 per pixel |
| Floating-point ops | Division + multiply | Addition only |
| Speed | Slow | Moderate |

---

### Exp 04 — Bresenham's Line Algorithm

> **Files:** `exp04_bresenham_line.cpp` | `exp04_bresenham_line.py`

#### Theory

**Bresenham's algorithm** uses **only integer arithmetic** — the fastest line drawing method.

```
BRESENHAM'S LINE ALGORITHM:

  dx = |x₂ - x₁|,  dy = |y₂ - y₁|
  sx = sign(x₂ - x₁),  sy = sign(y₂ - y₁)

  // If line is steep (dy > dx), swap dx and dy
  swapped = (dy > dx)
  if swapped: swap(dx, dy)

  // Decision parameter
  p = 2·dy - dx

  x = x₁, y = y₁

  for i = 0 to dx:
      plot(x, y)
      if p ≥ 0:
          if swapped: x += sx
          else:       y += sy
          p -= 2·dx
      if swapped: y += sy
      else:       x += sx
      p += 2·dy
```

#### Decision Parameter Logic

```
        p < 0                    p ≥ 0
     ┌─────────┐             ┌─────────┐
     │ Stay on │             │ Move to │
     │ same y  │             │ next y  │
     │ (or x)  │             │ (or x)  │
     └─────────┘             └─────────┘

  The decision parameter tells us which pixel
  is closer to the true line — the one directly
  to the right, or the one diagonally above-right.
```

#### Advantages

- **Integer arithmetic only** — no floating point
- **No multiplication/division** — fast on all hardware
- **Symmetric** — works in all 8 octants

---

### Exp 05 — Midpoint Circle Algorithm

> **Files:** `exp05_midpoint_circle.cpp` | `exp05_midpoint_circle.py`

#### Theory

Based on Bresenham's line algorithm, this uses the **symmetry of circles** to plot 8 points at once.

```
CIRCLE SYMMETRY (8-way):

                    (x, y)
                 ╱    │    ╲
               ╱      │      ╲
  (y, x) ────●────────┼────────●────(-y, x)
             │        │        │
             │   (xc,yc) center│
             │        │        │
  (-y, x) ──●────────┼────────●────(y, -x)
               ╲      │      ╱
                 ╲    │    ╱
                   (-x, y)

  For every point (x, y) computed, plot all 8:
  (±x ±y, ±y ±x) relative to center
```

#### Algorithm

```
MIDPOINT CIRCLE:

  x = 0,  y = r
  p = 1 - r          // initial decision parameter

  while x < y:
      plot 8 symmetric points at (x, y)
      x += 1
      if p < 0:
          p += 2·x + 3
      else:
          y -= 1
          p += 2·(x - y) + 5
```

---

### Exp 06 — 2D Translation

> **Files:** `exp06_translation.cpp` | `exp06_translation.py`

#### Theory

Translation moves every point of a shape by a constant offset.

```
TRANSLATION FORMULA:

  x' = x + tx
  y' = y + ty

  where (tx, ty) = translation vector

  In matrix form:
  ┌     ┐   ┌          ┐   ┌   ┐   ┌    ┐
  │ x'  │ = │ 1  0  tx │   │ x │   │ tx │
  │ y'  │   │ 0  1  ty │ × │ y │ + │ ty │
  │ 1   │   │ 0  0  1  │   │ 1 │   │ 0  │
  └     ┘   └          ┘   └   ┘   └    ┘
```

#### Visual

```
  Original          Translated (+100, +80)

    A●                  A'●
    │╲                    │╲
    │  ╲                  │  ╲
    │    ╲                │    ╲
    B──────C              B'──────C'

  Translation vector: ─────────▶
                        (100, 80)
```

---

### Exp 07 — 2D Rotation

> **Files:** `exp07_rotation.cpp` | `exp07_rotation.py`

#### Theory

Rotation rotates every point around a pivot by an angle θ.

```
ROTATION FORMULA (about origin):

  x' = x·cos(θ) - y·sin(θ)
  y' = x·sin(θ) + y·cos(θ)

  Matrix form:
  ┌     ┐   ┌               ┐   ┌   ┐
  │ x'  │ = │ cos(θ)  -sin(θ)│   │ x │
  │ y'  │   │ sin(θ)   cos(θ)│ × │ y │
  └     ┘   └               ┘   └   ┘

  For rotation about arbitrary point (cx, cy):
  1. Translate: x -= cx, y -= cy
  2. Rotate
  3. Translate back: x' += cx, y' += cy
```

#### Visual

```
         y
         │      ● Original point
         │     ╱
         │    ╱  θ = 45°
         │   ╱
         │  ● Rotated point
         │
  ───────┼───────── x
         │
  Rotation about origin:
  (1, 0) ──45°──▶ (0.707, 0.707)
```

---

### Exp 08 — 2D Scaling

> **Files:** `exp08_scaling.cpp` | `exp08_scaling.py`

#### Theory

Scaling changes the size of an object relative to a fixed point.

```
SCALING FORMULA (from center fx, fy):

  x' = fx + (x - fx) · sx
  y' = fy + (y - fy) · sy

  where (sx, sy) = scaling factors

  Uniform scaling:     sx = sy (proportional)
  Non-uniform scaling: sx ≠ sy (stretched)

  Matrix form (about origin):
  ┌     ┐   ┌         ┐   ┌   ┐
  │ x'  │ = │ sx  0  │   │ x │
  │ y'  │   │ 0   sy │ × │ y │
  └     ┘   └         ┘   └   ┘
```

#### Visual

```
  Original (100×100)     Scaled 1.5x     Scaled (2x, 0.5x)

    ┌──────┐              ┌────────────┐    ┌────────────────┐
    │      │              │            │    │                │
    │      │              │            │    └────────────────┘
    └──────┘              │            │
                          └────────────┘

  1.5× uniform:          2× width, 0.5× height
  (wider & taller)       (wider & shorter)
```

---

### Exp 09 — 3D Rotation About Arbitrary Axis

> **Files:** `exp09_3d_rotation.cpp` | `exp09_3d_rotation.py`

#### Theory

Rotating a 3D object about **any line in space** (not just x, y, z axes) uses **Rodrigues' Rotation Formula**.

```
RODRIGUES' FORMULA:

  v' = v·cos(θ) + (u × v)·sin(θ) + u·(u·v)·(1 - cos(θ))

  where:
    v = point to rotate (as vector from axis)
    u = unit vector along rotation axis
    θ = rotation angle
    × = cross product
    · = dot product
```

#### Steps

```
┌─────────────────────────────────────────────────┐
│  STEP 1: Translate so axis passes through origin │
│          p' = p - a₁                             │
│                                                  │
│  STEP 2: Normalize axis direction                │
│          u = (a₂ - a₁) / |a₂ - a₁|             │
│                                                  │
│  STEP 3: Apply Rodrigues' formula                │
│          v' = v·cosθ + (u×v)·sinθ + u·(u·v)·(1-cosθ)│
│                                                  │
│  STEP 4: Translate back                          │
│          p'' = p' + a₁                           │
└─────────────────────────────────────────────────┘
```

#### 3D-to-2D Projection (Oblique)

```
  screen_x = world_x + world_z × 0.5 × cos(30°)
  screen_y = world_y + world_z × 0.5 × sin(30°)

  ┌────────────────────┐
  │    Z axis          │
  │     ╱              │
  │    ╱  30°          │  Oblique projection
  │   ╱                │  gives pseudo-3D effect
  │  ●─────── X axis   │
  │  │                 │
  │  │ Y axis          │
  │  │                 │
  └────────────────────┘
```

---

### Exp 10 — Cohen-Sutherland Line Clipping

> **Files:** `exp10_cohen_sutherland.cpp` | `exp10_cohen_sutherland.py`

#### Theory

**Cohen-Sutherland** clips a line against a rectangular window using **outcodes**.

```
OUTCODE ASSIGNMENT:

         1001 │ 1000 │ 1010
         ─────┼──────┼─────
              │      │
         0001 │ 0000 │ 0010
              │      │
         ─────┼──────┼─────
         0101 │ 0100 │ 0110

  Bit 0 (1): LEFT   (x < xmin)
  Bit 1 (2): RIGHT  (x > xmax)
  Bit 2 (4): BOTTOM (y > ymax)  [y increases downward]
  Bit 3 (8): TOP    (y < ymin)
```

#### Algorithm

```
COHEN-SUTHERLAND:

  code1 = compute_code(x1, y1)
  code2 = compute_code(x2, y2)

  LOOP:
    if both codes == 0:
        ACCEPT — line is fully inside
    else if code1 & code2 ≠ 0:
        REJECT — both endpoints outside same edge
    else:
        clip against the edge where one endpoint is outside
        update endpoint and its outcode
```

#### Decision Flow

```
         Start
           │
     ┌─────▼─────┐
     │ code1=0 &  │    YES
     │ code2=0?  ├────────▶ ACCEPT (fully inside)
     └─────┬─────┘
           │ NO
     ┌─────▼──────┐
     │ code1 &    │    YES
     │ code2 ≠ 0? ├────────▶ REJECT (fully outside)
     └─────┬──────┘
           │ NO
     ┌─────▼──────────┐
     │ Clip endpoint  │
     │ against boundary│
     └─────┬──────────┘
           │
           └──▶ Back to LOOP
```

---

### Exp 11 — Sutherland-Hodgman Polygon Clipping

> **Files:** `exp11_sutherland_hodgman.cpp` | `exp11_sutherland_hodgman.py`

#### Theory

**Sutherland-Hodgman** clips a polygon against each edge of the clipping window sequentially.

```
CLIPPING AGAINST ONE EDGE:

  For each edge (S→E) of the polygon:
    ┌────────────────────────────────────────┐
    │ Both inside:    → Add E to output      │
    │ S inside, E out → Add intersection     │
    │ S out, E inside → Add intersection, E  │
    │ Both outside:   → Nothing              │
    └────────────────────────────────────────┘

  Repeat for all 4 edges of the clipping window:
  LEFT → RIGHT → BOTTOM → TOP
```

#### Visual

```
  Original Polygon          After Clipping
       ╱╲                      ╱╲
      ╱  ╲                    ╱  ╲
     ╱    ╲                  ╱    ╲
    ╱  ┌───┼──┐             ╱ ┌───┐╲
   ╱   │   │  ╲           ╱  │   │ ╲
  ╱────┼───┼───╲         ╱───┼───│──╲
       │   │              │   │
       └───┘              └───┘

  Polygon extends outside → clipped to window
```

---

### Exp 12 — Bézier Curves

> **Files:** `exp12_bezier.cpp` | `exp12_bezier.py`

#### Theory

A **Bézier curve** is a parametric curve defined by control points using **Bernstein polynomials**.

```
CUBIC BÉZIER (4 control points P0-P3):

  B(t) = (1-t)³·P₀ + 3t(1-t)²·P₁ + 3t²(1-t)·P₂ + t³·P₃

  where t ∈ [0, 1]

  BERNSTEIN BASIS FUNCTIONS:
    B₀(t) = (1-t)³
    B₁(t) = 3t(1-t)²
    B₂(t) = 3t²(1-t)
    B₃(t) = t³
```

#### Properties

```
  ● P₀ (start)                      Properties:
  │                                  • Passes through P₀ and P₃
  │  ● P₁ (control)                 • Tangent to P₀P₁ at start
  │  │                              • Tangent to P₂P₃ at end
  │  │  ● P₂ (control)             • Bounded by convex hull
  │  │  │                           • C¹ continuous (smooth)
  │  │  │
  │  │  │  ● P₃ (end)
  │  │  │  │
  ╱╱╱╱╱╱╱╱
  Bézier Curve
```

---

### Exp 13 — B-Spline Curves

> **Files:** `exp13_b_spline.cpp` | `exp13_b_spline.py`

#### Theory

**B-Splines** extend Bézier curves by providing **local control** — moving one control point only affects a portion of the curve.

```
UNIFORM CUBIC B-SPLINE BASIS:

  N₀(t) = (-t³ + 3t² - 3t + 1) / 6
  N₁(t) = (3t³ - 6t² + 4) / 6
  N₂(t) = (-3t³ + 3t² + 3t + 1) / 6
  N₃(t) = t³ / 6

  Curve segment i uses control points: Pᵢ, Pᵢ₊₁, Pᵢ₊₂, Pᵢ₊₃
```

#### B-Spline vs Bézier

| Feature | Bézier | B-Spline |
|---------|--------|----------|
| Control points | 4 | Any number (n ≥ 4) |
| Passes through endpoints | Yes | No (usually) |
| Local control | No | Yes |
| Continuity | C¹ | C² |
| Smoothness | Good | Better |

```
  CONTROL POINTS              BÉZIER                    B-SPLINE
  ●───●───●───●              ●═══════●                 ●═══●═══●═══●
  P0  P1  P2  P3           (single curve)           (piecewise smooth)
                                          
  Moving P2 affects:        Entire curve changes      Only local region
```

---

## File Structure

```
computer-graphics/lab/
├── README.md                          ← This file
├── LICENSE                            ← MIT License
├── index.html                         ← Interactive lab menu (web)
│
├── exp01_io_devices.md                ← Theory: I/O devices
├── exp02_slope_intercept.cpp/.py      ← Slope-intercept line drawing
├── exp03_dda_line.cpp/.py             ← DDA line algorithm
├── exp04_bresenham_line.cpp/.py       ← Bresenham's line algorithm
├── exp05_midpoint_circle.cpp/.py      ← Midpoint circle algorithm
├── exp06_translation.cpp/.py          ← 2D translation
├── exp07_rotation.cpp/.py             ← 2D rotation
├── exp08_scaling.cpp/.py              ← 2D scaling
├── exp09_3d_rotation.cpp/.py          ← 3D rotation (Rodrigues')
├── exp10_cohen_sutherland.cpp/.py     ← Cohen-Sutherland line clipping
├── exp11_sutherland_hodgman.cpp/.py   ← Sutherland-Hodgman polygon clipping
├── exp12_bezier.cpp/.py              ← Cubic Bézier curves
├── exp13_b_spline.cpp/.py            ← Uniform cubic B-Spline curves
│
├── setup.ps1                          ← Environment setup script
├── run.ps1                            ← Compile & run a single experiment
├── run.bat                            ← Batch version of run.ps1
├── menu.ps1                           ← Interactive experiment selector
├── menu.bat                           ← Batch version of menu.ps1
├── render_all.py                      ← Render all Python experiments
├── frame_screenshot.py                ← Capture frames as images
│
├── include/                           ← BGI headers & library
│   ├── graphics.h
│   ├── winbgim.h
│   └── libbgi.a
│
├── assets/                            ← Screenshots and images
└── .vscode/                           ← VS Code configuration
```

---

## Running in VS Code

The `.vscode/` directory contains pre-configured tasks:

1. Open the lab folder in VS Code
2. Press `Ctrl+Shift+B` to build the current experiment
3. Press `F5` to run with debugging

---

## References

- **Hearn, D. & Baker, M.P.** — *Computer Graphics with OpenGL*
- **Foley, J.D. van Dam et al.** — *Computer Graphics: Principles and Practice*
- **Donald Hearn** — *Computer Graphics C Version*
- [OpenGL Documentation](https://docs.gl/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

---

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center">
  Made with purpose for Computer Graphics coursework
  <br>
  <a href="https://github.com/PavelGoblin/academics">Back to Academics Repository</a>
</p>
