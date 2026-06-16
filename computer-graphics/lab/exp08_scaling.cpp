// ===================================================================
// Experiment 08: 2D Scaling Transformation
//
// THEORY:
// Scaling changes the SIZE of an object by multiplying coordinates
// by scaling factors sx and sy.
//
// FORMULA (scaling about origin):
//   x' = x × sx
//   y' = y × sy
//
// MATRIX FORM:
//   | x' |   | sx  0   0 |   | x |
//   | y' | = | 0   sy  0 | * | y |
//   | 1  |   | 0   0   1 |   | 1 |
//
// SCALING ABOUT A FIXED POINT (fx, fy):
// Like rotation, we can't just multiply about any point.
// Steps:
//   1. TRANSLATE so fixed point → origin:   T(-fx, -fy)
//   2. SCALE about origin:                   S(sx, sy)
//   3. TRANSLATE back:                       T(fx, fy)
//
// Combined:  P' = T(fx, fy) · S(sx, sy) · T(-fx, -fy) · P
//
// In code:  x_rel = x - fx,  y_rel = y - fy
//           x_new = fx + x_rel × sx
//           y_new = fy + y_rel × sy
//
// UNIFORM vs DIFFERENTIAL:
//   Uniform: sx = sy → object keeps proportions
//   Differential: sx ≠ sy → object stretches/distorts
// ===================================================================

#include <graphics.h>
#include <cmath>         // For round()
#include <conio.h>
#include <cstdio>

// Helper: Draw a triangle
void drawTriangle(int x1, int y1, int x2, int y2, int x3, int y3, int color) {
    setcolor(color);
    line(x1, y1, x2, y2);
    line(x2, y2, x3, y3);
    line(x3, y3, x1, y1);
}

// Helper: Draw a rectangle (just uses built-in rectangle())
void drawRect(int x1, int y1, int x2, int y2, int color) {
    setcolor(color);
    rectangle(x1, y1, x2, y2);
}

// Function: Scale a point about a fixed point (fx, fy)
// (x, y) = original point
// (sx, sy) = scaling factors
// (xOut, yOut) = scaled point
void scalePoint(int x, int y, int fx, int fy, float sx, float sy, int &xOut, int &yOut) {
    // x_rel = distance of point from fixed point
    // Multiply by sx to scale → add back to fixed point
    xOut = fx + (int)((x - fx) * sx + 0.5f);
    yOut = fy + (int)((y - fy) * sy + 0.5f);
}

// ===================================================================
// MAIN FUNCTION
// ===================================================================
int main() {
    float sx1, sy1, sx2, sy2, triSx, triSy;
    printf("=== 2D Scaling Transformation ===\n");
    printf("Rectangle uniform scale factor (sx sy): ");
    scanf("%f %f", &sx1, &sy1);
    printf("Rectangle differential scale (sx sy): ");
    scanf("%f %f", &sx2, &sy2);
    printf("Triangle scale factor (sx sy): ");
    scanf("%f %f", &triSx, &triSy);

    initwindow(640, 480, "2D Scaling Transformation");

    // ================================================================
    // PART 1: Scale a RECTANGLE
    // ================================================================
    // Original rectangle (top-left and bottom-right)
    int rx1 = 50, ry1 = 50;
    int rx2 = 150, ry2 = 150;

    // Fixed point = center of rectangle
    int fx = (rx1 + rx2) / 2;    // Center X
    int fy = (ry1 + ry2) / 2;    // Center Y

    // Draw original (WHITE)
    drawRect(rx1, ry1, rx2, ry2, WHITE);
    outtextxy(rx1, ry1 - 15, "Original");

    // UNIFORM SCALING with user factor
    int nrx1, nry1, nrx2, nry2;
    scalePoint(rx1, ry1, fx, fy, sx1, sy1, nrx1, nry1);
    scalePoint(rx2, ry2, fx, fy, sx1, sy1, nrx2, nry2);
    drawRect(nrx1, nry1, nrx2, nry2, YELLOW);
    char lbl1[64]; sprintf(lbl1, "Scaled %.1fx,%.1fy (uniform)", sx1, sy1);
    outtextxy(nrx1, nry1 - 15, lbl1);

    // DIFFERENTIAL SCALING with user factors
    scalePoint(rx1, ry1, fx, fy, sx2, sy2, nrx1, nry1);
    scalePoint(rx2, ry2, fx, fy, sx2, sy2, nrx2, nry2);
    drawRect(nrx1, nry1, nrx2, nry2, CYAN);
    char lbl2[64]; sprintf(lbl2, "Scaled (%.1fx, %.1fy) (diff)", sx2, sy2);
    outtextxy(nrx1, nry1 - 15, lbl2);

    // ================================================================
    // PART 2: Scale a TRIANGLE
    // ================================================================
    // Triangle vertices
    int x1 = 350, y1 = 80;      // Top
    int x2 = 450, y2 = 200;     // Right
    int x3 = 250, y3 = 200;     // Left

    // Centroid = fixed point for scaling
    int tfx = (x1 + x2 + x3) / 3;
    int tfy = (y1 + y2 + y3) / 3;

    // Original triangle
    drawTriangle(x1, y1, x2, y2, x3, y3, WHITE);
    outtextxy(tfx - 20, tfy, "Original");

    // Scale triangle with user factor
    int nx1, ny1, nx2, ny2, nx3, ny3;
    scalePoint(x1, y1, tfx, tfy, triSx, triSy, nx1, ny1);
    scalePoint(x2, y2, tfx, tfy, triSx, triSy, nx2, ny2);
    scalePoint(x3, y3, tfx, tfy, triSx, triSy, nx3, ny3);
    drawTriangle(nx1, ny1, nx2, ny2, nx3, ny3, MAGENTA);
    char lbl3[64]; sprintf(lbl3, "Scaled %.1fx", triSx);
    outtextxy(tfx - 20, tfy + 100, lbl3);

    outtextxy(10, 10, "Experiment 08: 2D Scaling Transformation");
    outtextxy(10, 30, "Uniform & Differential Scaling about Center");

    getch();
    closegraph();
    return 0;
}
