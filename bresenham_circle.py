from graphics import *


def draw_circle_points(xc, yc, x, y, win):
    points = [
        (xc + x, yc + y), (xc - x, yc + y), (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x), (xc + y, yc - x), (xc - y, yc - x)
    ]
    for px, py in points:
        pt = Point(px, py)
        pt.setFill("red")
        pt.draw(win)


def bresenham_circle(xc, yc, r, win):
    x = 0
    y = r
    d = 3 - 2 * r

    draw_circle_points(xc, yc, x, y, win)

    while y >= x:
        x += 1
        if d > 0:
            y -= 1
            d += 4 * (x - y) + 10
        else:
            d += 4 * x + 6
        draw_circle_points(xc, yc, x, y, win)


def main():
    width, height = 800, 600
    win = GraphWin("Bresenham's Circle", width, height)
    win.setBackground("white")

    xc, yc, r = 400, 300, 100

    bresenham_circle(xc, yc, r, win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
