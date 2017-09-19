#zelle 10.7 text example - animated cannonball

from graphics import *
from zelle_10_7_shottracker import ShotTracker
from math import atan, sqrt, pi

def fire(win, pt, aimLine):
    #gather inputs
    x, y = pt.getX(), pt.getY()
    h = 0.001
    a = atan(y/x) * 180 / pi
    v = sqrt(x**2 + y**2) * 1.5

    #draw aim line
    aimLine.undraw()
    aimLine = Line(Point(0,0), pt)
    aimLine.setArrow('last')
    aimLine.draw(win)

    #fire cannonball
    return ShotTracker(win, h, a, v), aimLine
        
def main():

    #create window
    win = GraphWin('Cannonball Animation', 640, 480, autoflush=False)
    win.setCoords(-10, -10, 210, 155)

    #draw baseline
    Line(Point(-10,0), Point(210,0)).draw(win)

    #draw ticks and labels
    for i in range(0,210,50):
        Text(Point(i, -5), str(i)).draw(win)
        Line(Point(i, 2), Point(i, 2)).draw(win)

    #main event loop
    shots = []
    pt = None
    aimLine = Line(Point(0,0),Point(0,0))
    launcher = ShotTracker(win,0,0,0)
    while True:
        pt = win.checkMouse()
        if pt:
            latest, aimLine = fire(win, pt, aimLine)
            shots.append(latest)
        for s in shots:
            if s.getY()>0 and -10<s.getX()<210:
                s.update(1/50)
            else:
                s.undraw()
        update(50)
    
        
    win.close()

if __name__ == '__main__': main()
