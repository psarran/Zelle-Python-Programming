#zelle 10.9.3 - three button monte

from zelle_10_6_1_button import Button
from random import randrange
from graphics import *

def setup():
    #draw window
    win = GraphWin('Three Button Monte', 500, 500)
    win.setCoords(0,0,10,10)
    door1 = Button(win, Point(2.5, 5), 2, 4, '1')
    door2 = Button(win, Point(  5, 5), 2, 4, '2')
    door3 = Button(win, Point(7.5, 5), 2, 4, '3')
    qt = Button(win, Point(5, 1.5), 4, 1, 'Quit')
    header =        Text(Point(5, 8.5), 'Click on a door to guess')
    winLabel =      Text(Point(7.5, 8.75), 'W')
    lossLabel =     Text(Point(8.5, 8.75), 'L')
    winsCounter =   Text(Point(7.5, 8.25), '0')
    lossesCounter = Text(Point(8.5, 8.25), '0')
    line1 = Line(Point(7,8.5), Point(9,8.5))    
    line2 = Line(Point(8,9), Point(8,8))

    door1.activate()
    door2.activate()
    door3.activate()
    qt.activate()

    header.draw(win)
    winLabel.draw(win)
    lossLabel.draw(win)
    winsCounter.draw(win)
    lossesCounter.draw(win)
    line1.draw(win)
    line2.draw(win)

    return win, door1, door2, door3, qt, header, winsCounter, lossesCounter

def game(win, door1, door2, door3, qt):
    prize = randrange(1,4)
    end = False
    pt = win.getMouse()
    guess = 0
    while True:
        if qt.clicked(pt):
            end = True
            break
        if door1.clicked(pt):
            guess = 1
            break
        if door2.clicked(pt):
            guess = 2
            break
        if door3.clicked(pt):
            guess = 4
            break
        pt = win.getMouse()
    if prize == guess:
        return True, end, prize
    else:
        return False, end, prize
    
def main():
    win, door1, door2, door3, qt, header, winsCounter, lossesCounter = setup()
    end = False
    wins, losses = 0, 0
    
    while not end:
        result, end, prize = game(win, door1, door2, door3, qt)
        print(prize)
        if result:
            wins += 1
            winsCounter.setText(str(wins))
            header.setText('Correct!')
        else:
            losses += 1
            lossesCounter.setText(str(losses))
            header.setText('Wrong! Correct door was #{0:0.0f}'.format(prize))

    win.close()

if __name__ == '__main__': main()
