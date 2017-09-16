#zelle 10.6.1 text example - dice - roller.py

from graphics import GraphWin, Point
from random import randrange
from zelle_10_6_1_button import Button
from zelle_10_6_1_dieview import DieView

def main():
    #draw main window
    win = GraphWin('Dice Roller', 500, 500)
    win.setCoords(0, 0, 10, 10)
    win.setBackground('green2')

    #draw die and buttons
    die1 = DieView(win, Point(3,6.5), 2)
    die2 = DieView(win, Point(7,6.5), 2)
    rollButton = Button(win, Point(3,2.5), 4, 1, 'Roll Dice')
    rollButton.activate()
    quitButton = Button(win, Point(8,2.5), 2, 1, 'Quit')


    #event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            a, b = randrange(1,7), randrange(1,7)
            die1.setValue(a)
            die2.setValue(b)
            quitButton.activate()
            pt = win.getMouse()

    #clean up
    win.close()

if __name__ == '__main__': main()
