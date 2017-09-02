#zelle 7.7.16 archery score

from graphics import *
from math import *

def drawBoard():
    win = GraphWin('archery')
    win.setCoords(0,0,100,100)

    whiteCirc = Circle(Point(50,50),8 * 5)
    whiteCirc.setFill('white')
    whiteCirc.draw(win)

    blackCirc = Circle(Point(50,50),8 * 4)
    blackCirc.setFill('black')
    blackCirc.draw(win)

    blueCirc = Circle(Point(50,50),8 * 3)
    blueCirc.setFill('blue')
    blueCirc.draw(win)

    redCirc = Circle(Point(50,50),8 * 2)
    redCirc.setFill('red')
    redCirc.draw(win)

    yellowCirc = Circle(Point(50,50),8)
    yellowCirc.setFill('yellow')
    yellowCirc.draw(win)

    return win

def main():
    win = drawBoard()

    score = 0
    
    for i in range(5):
        shot = win.getMouse()
        shot.draw(win)
        r = sqrt( (shot.getY()-50) ** 2 + (shot.getX() - 50) ** 2 )
        if r <= 8:
            points = 9
        elif r <= 16:
            points = 7
        elif r <= 24:
            points = 5
        elif r <= 32:
            points = 3
        elif r <= 40:
            points = 1
        else:
            points = 0
        score += points
        print('current score: {0:0}'.format(score))

main()
