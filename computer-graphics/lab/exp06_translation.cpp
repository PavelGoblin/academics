// ===================================================================
// Experiment 06: 2D Translation of a Line and Triangle
//
// THEORY:
// Translation moves every point of an object by the same distance.
// It's the SIMPLEST geometric transformation!
//
// FORMULA:
//   x_new = x_old + tx     (tx = translation distance in x)
//   y_new = y_old + ty     (ty = translation distance in y)
//
// MATRIX FORM (Homogeneous coordinates):
//   | x' |   | 1 0 tx |   | x |
//   | y' | = | 0 1 ty | * | y |
//   | 1  |   | 0 0 1  |   | 1 |
//
// VISUAL:
//   Before:     After:
//     ▲           ▲
//    / \         / \
//   /   \   →   /   \
//  /     \     /     \
//  ───────     ───────  (shifted right by tx, down by ty)
//
// To translate an object: translate EVERY vertex, then redraw
// ===================================================================

#include <graphics.h>    // Graphics functions
#include <conio.h>       // For getch()
#include <cstdio>        // For sprintf() to format text labels

// Helper: Draw a triangle given its 3 vertices
// color = line color (WHITE, YELLOW, CYAN, etc.)
void drawTriangle(int x1, int y1, int x2, int y2, int x3, int y3, int color) {
    setcolor(color);
    line(x1, y1, x2, y2);    // Edge 1: vertex 1 → vertex 2
    line(x2, y2, x3, y3);    // Edge 2: vertex 2 → vertex 3
    line(x3, y3, x1, y1);    // Edge 3: vertex 3 → vertex 1
}

// Helper: Draw a line between two points
void drawLine(int x1, int y1, int x2, int y2, int color) {
    setcolor(color);
    line(x1, y1, x2, y2);
}

// ===================================================================
// MAIN FUNCTION
// ===================================================================
int main() {
    int tx, ty, triTx, triTy;
    printf("=== 2D Translation Transformation ===\n");
    printf("Line translation (tx ty): ");
    scanf("%d %d", &tx, &ty);
    printf("Triangle translation (tx ty): ");
    scanf("%d %d", &triTx, &triTy);

    initwindow(640, 480, "2D Translation Transformation");

    // ================================================================
    // PART 1: Translate a LINE
    // ================================================================
    // Original line (in WHITE)
    int lx1 = 50, ly1 = 50;     // Line start
    int lx2 = 200, ly2 = 150;   // Line end
    drawLine(lx1, ly1, lx2, ly2, WHITE);
    outtextxy(lx1, ly1 - 20, "Original Line");

    // Translated line (in YELLOW)
    drawLine(lx1 + tx, ly1 + ty,
             lx2 + tx, ly2 + ty,
             YELLOW);
    char label[50];
    sprintf(label, "Translated (tx=%d, ty=%d)", tx, ty);
    outtextxy(lx1 + tx, ly1 + ty - 20, label);

    // ================================================================
    // PART 2: Translate a TRIANGLE
    // ================================================================
    // Original triangle vertices (in WHITE)
    int x1 = 300, y1 = 100;     // Top vertex
    int x2 = 400, y2 = 250;     // Bottom-right vertex
    int x3 = 200, y3 = 250;     // Bottom-left vertex
    drawTriangle(x1, y1, x2, y2, x3, y3, WHITE);
    outtextxy(x1 - 30, y1 - 20, "Original Triangle");

    // Translated triangle (in CYAN)
    drawTriangle(
        x1 + triTx, y1 + triTy,
        x2 + triTx, y2 + triTy,
        x3 + triTx, y3 + triTy,
        CYAN
    );
    sprintf(label, "Translated (tx=%d, ty=%d)", triTx, triTy);
    outtextxy(x1 + triTx - 30, y1 + triTy - 20, label);

    // Labels
    outtextxy(10, 10, "Experiment 06: 2D Translation");
    outtextxy(10, 30, "White = Original | Yellow/Cyan = Translated");

    getch();
    closegraph();
    return 0;
}
