#zelle 12.3 text exercise - dice game interface

from zelle_10_6_1_button import Button
from zelle_12_3_dieview import DieView
from graphics import *

class PokerInterface():
    """ GUI interface to place the dice poker game """

    def __init__(self):
        self.win = GraphWin('Poker', 600, 400)
        self.win.setBackground('green3')
        
        banner = Text(Point(300, 30), 'Python Dice Poker')
        banner.setSize(24)
        banner.setTextColor('yellow2')
        banner.setStyle('bold')
        banner.draw(self.win)
        
        self.buttons = []
        b = Button(self.win, Point(300,230), 400, 40, 'Roll Dice')
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, 'Score')
        self.buttons.append(b)
        b = Button(self.win, Point(570, 375), 40, 30, 'Quit')
        self.buttons.append(b)
        
        self.createDice(Point(300,100), 75)
        self.addDiceButtons(Point(300,170), 75, 30)

        self.msg = Text(Point(300, 380), 'Welcome to Python Dice Poker')
        self.msg.setSize(18)
        self.msg.draw(self.win)

        self.wallet = Text(Point(300, 325), '${0}'.format(100))
        self.wallet.setSize(18)
        self.wallet.draw(self.win)

    def createDice(self, center, size):
        center.move(-size*3,0)
        self.dice = []
        for i in range(5):
            d = DieView(self.win, center, size)
            self.dice.append(d)
            center.move(size*1.5, 0)

    def addDiceButtons(self, center, width, height):
        center.move(-width*3,0)
        for i in range(5):
            b = Button(self.win, center, width, height, 'Die '+str(i+1))
            self.buttons.append(b)
            center.move(width*1.5, 0)

    def setWallet(self, wallet):
        self.wallet.setText('${0}'.format(wallet))

    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])
    
    def chooseDice(self):
        toRoll = []
        choices = []
        while True:
            for b in self.buttons:
                choices.append(b.getLabel())
            if toRoll == []:
                choices.remove('Roll Dice')
            b = self.choose(choices)
            if b[0] == 'D':
                if int(b[4])-1 in toRoll:
                    toRoll.remove(int(b[4])-1)
                    self.dice[int(b[4])-1].setColor('black')
                else:
                    toRoll.append(int(b[4])-1)
                    self.dice[int(b[4])-1].setColor('grey')
            elif b == 'Quit':
                self.close()
                break
            else:
                for d in self.dice:
                    d.setColor('black')
                return toRoll

    def choose(self, choices):
        buttons = self.buttons

        #activate only the appropriate buttons
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        #wait until user clicks one of the button choices,
        #then return that button label
        while True:
            pt = self.win.getMouse()
            for b in buttons:
                if b.clicked(pt):
                    return b.getLabel()
        
    def showResult(self, hand, payout):
        if payout > 0:
            self.msg.setText('You rolled a {0}. Payout: ${1}'.format(hand, payout))
        else:
            self.msg.setText('Crap Hand')

    def wantToPlay(self):
        ans = self.choose(['Roll Dice', 'Quit'])
        self.msg.setText('')
        return ans == 'Roll Dice'
    
    def close(self):
        self.win.close()


class TextPokerInterface():
    """ Text based interface to place the dice poker game """

    def __init__(self):
        print('Here we go...')

    def setWallet(self, wallet):
        print('Current cash:', wallet)

    def setDice(self, values):
        print('Current roll is:', values)
    
    def chooseDice(self):
        toRoll = eval(input('Which dice do you want to re-roll?'))
        return toRoll

    def showResult(self, hand, payout):
        print('You rolled a', hand + '.')
        print('Payout is', payout)

    def wantToPlay(self):
        play = input('Do you want to play (y/n)?')
        return play == 'y'
    
    def close(self):
        print('Thanks for playing')
