#zelle 12.3 text exercise - dice poker

from zelle_12_3_dice import Dice
from zelle_12_3_pokerinterface import TextPokerInterface, PokerInterface

class PokerApp():
    """ a game to play poker with 5 dice
        Player starts with $100
        Rolls 5 dice
        Then gets two chances to roll any or all dice again
        Each hand costs $10 to play
    """
    
    def __init__(self, interface):
        self.dice = Dice()
        self.wallet = 100
        self.interface = interface

    def playHand(self):
        self.wallet -= 10
        self.interface.setWallet(self.wallet)
        self.doRolls()
        hand, payout = self.dice.score()
        self.wallet += payout
        self.interface.showResult(hand, payout)
        self.interface.setWallet(self.wallet)

    def doRolls(self):
        self.dice.rollAll()
        rolls = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while rolls < 3 and toRoll != []:
            self.dice.roll(toRoll)
            self.interface.setDice(self.dice.values())
            rolls += 1
            if rolls < 3:
                toRoll = self.interface.chooseDice()
            
    def run(self):
        while self.wallet >= 10 and self.interface.wantToPlay():
            self.playHand()
        self.interface.close()


if __name__ == '__main__':
    interface = PokerInterface()
    theGame = PokerApp(interface)
    theGame.run()
