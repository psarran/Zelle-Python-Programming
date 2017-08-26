#zelle 4.7.1 in-text exercise - draw triangle

from graphics import *

def main():
    win = GraphWin('triangle')
    win.setCoords(0.0,0.0, 10.0,10.0)

    message = Text(Point(5, 0.5), 'click three places')
    message.draw(win)

    p1 = win.getMouse()
    #p1.draw(win)
    k1 = win.getKey()
    l1 = Text(p1,k1)
    l1.draw(win)

    p2 = win.getMouse()
    #p2.draw(win)
    k2 = win.getKey()
    l2 = Text(p2,k2)
    l2.draw(win)

    p3 = win.getMouse()
    #p3.draw(win)
    k3 = win.getKey()
    l3 = Text(p3,k3)
    l3.draw(win)

    tri = Polygon(p1, p2, p3)
    tri.setFill('peachpuff')
    tri.setOutline('cyan')
    tri.draw(win)

    message.setText('click to quit')
    win.getMouse()
    message.setText('')
main()
