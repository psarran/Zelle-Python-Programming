#zelle 7.7.17 bouncing circle

from graphics import *
from math import *

def main():
    win = GraphWin('bouncing circle', 500, 300)
    circ = Circle(Point(50, 50), 10)
    circ.draw(win)

    dx, dy = 2, 2

    for i in range(1000):
        circ.move(dx, dy)
        if circ.getCenter().getX() <= 10 or circ.getCenter().getX() >= 490:
            dx = -1 * dx
        if circ.getCenter().getY() <= 10 or circ.getCenter().getY() >= 290:
            dy = -1 * dy

main()
    
