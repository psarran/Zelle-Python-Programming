# Zelle 4.10.7

from graphics import *
import math

def main():

    circleR = float(input('radius: '))
    yInt = float(input('y-int: '))

    win = GraphWin('Circle Intersection')
    win.setCoords(-10,-10,10,10)

    circ = Circle(Point(0,0), circleR)
    circ.draw(win)

    line = Line(Point(-10,yInt),Point(10,yInt))
    line.draw(win)

    xInt2 =   math.sqrt(circleR ** 2 - yInt ** 2)
    xInt1 = - xInt2
        
    pt1 = Point(xInt1, yInt)
    pt2 = Point(xInt2, yInt)

    pt1.setFill('red')
    pt2.setFill('red')

    pt1.draw(win)
    pt2.draw(win)

    print('first int: ' + str(xInt1) + ' second int: ' + str(xInt2))

main()
