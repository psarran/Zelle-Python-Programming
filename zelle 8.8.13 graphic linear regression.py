#zelle 8.8.13 graphic linear regression

from graphics import *

def setup():
    win = GraphWin('linear regression', 500, 500)
    doneX1 = 4
    doneX2 = 50
    doneY1 = 496
    doneY2 = 470

    Rectangle(Point(doneX1, doneY1), Point(doneX2, doneY2)).draw(win)
    Text(Point(doneX1 + (doneX2 - doneX1)/2, doneY1 + (doneY2 - doneY1)/2), 'Done').draw(win)

    return win, doneX1, doneX2, doneY1, doneY2
    
def collectPts(win, doneX1, doneX2, doneY1, doneY2):
         
    x, y, xx, xy, n = 0, 0, 0, 0, 0 

    while True:
         pt = win.getMouse()
         ptX = pt.getX()
         ptY = pt.getY()
         
         if ptX >= doneX1 and ptX <= doneX2 and ptY <= doneY1 and ptY >= doneY2: break
 
         pt.draw(win)
         x += ptX
         y += ptY
         xx += ptX ** 2
         xy += ptX * ptY
         n += 1

    return x, y, xx, xy, n

def calcRegressionLine(x, y, xx, xy, n):

    b = (xy - x * y / n) / (xx - x ** 2 / n)

    line = Line(Point(0, y/n - b * x/n), Point(500, y/n + b * (500 - x/n) ))

    return line

def main():

    win, doneX1, doneX2, doneY1, doneY2 = setup()

    print('click in window to draw observations, click in \'done\' box to end')

    x, y, xx, xy, n = collectPts(win, doneX1, doneX2, doneY1, doneY2)
    line = calcRegressionLine(x, y, xx, xy, n)
    line.draw(win)

    print('click again to exit')
    win.getMouse()
    win.close()

main()
    
    
