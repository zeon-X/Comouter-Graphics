from graphics import *
import math


def scan_x(x):
    return round(x)


def scan_y(y, height):
    return height - round(y)


def main():
    # Create a graphics window
    width, height = 800, 600
    win = GraphWin("Line Drawing", width, height)
    win.setBackground("white")

    # Line coordinates
    x1, y1 = 10.5, 10.6
    x2, y2 = 100.3, 100.9

    # Calculate the slope of the line
    m = (y2 - y1) / (x2 - x1)

    # Initialize variables
    if m > 1.0:
        indep = y1
        dep = x1
        max_indep = y2
    else:
        indep = x1
        dep = y1
        max_indep = x2

    b = y1 - m * x1

    # Draw the line pixel by pixel
    while indep <= max_indep:
        indep += 1
        if m > 1.0:
            x = dep
            y = indep
            dep = (indep - b) / m
        else:
            x = indep
            y = dep
            dep = m * indep + b

        # Plot the pixel
        pt = Point(scan_x(x), scan_y(y, height))
        pt.setFill("red")
        pt.draw(win)

    # Wait for user interaction before closing
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
