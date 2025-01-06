from graphics import *


def genTable(x1, y1, x2, y2, dx, dy, p, win):

    pt = Point(x1, y1)
    pt.setFill("red")
    pt.draw(win)
    print(x1, x2)

    if x1 != x2 and y1 != y2:
        x1p = x1+1
        if p < 0:
            y1p = y1
            pp = p + 2*dy
        else:
            y1p = y1+1
            pp = p + 2*(dy-dx)
        genTable(x1p, y1p, x2, y2, dx, dy, pp, win)


def main():

    width, height = 800, 600
    win = GraphWin("Bresenham's Line", width, height)
    win.setBackground("white")

    x1, y1 = 50, 50
    x2, y2 = 300, 200

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2*dy-dx

    genTable(x1, y1, x2, y2, dx, dy, p, win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
