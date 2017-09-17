#zelle 10.7 text example - animated cannonball

from graphics import *
from zelle_10_7_shottracker import ShotTracker


def fire(win):       
    #get inputs
    h = float(input('launch height: '))
    v = float(input('launch velocity: '))
    a = float(input('launch angle (in degrees): '))

    #fire cannonball
    st = ShotTracker(win, h, a, v)
    while st.getY()>0 and -10 < st.getX() <= 210:
        st.update(1/50)
        update(50)

        
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

    q = False
    while not q:
        fire(win)
        q = 'y' != input('fire again? (y for another, anything else to quit): ')
        
    win.close()

if __name__ == '__main__': main()
