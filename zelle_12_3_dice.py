#zelle 12.3 text exercise - Dice class

from random import randrange
from zelle_10_6_1_dieview import DieView
from zelle_10_6_1_button import Button

class Dice():
    """ Collection of five dice for the dice poker game """

    def __init__(self):
        self.dice = [0] * 5
        self.rollAll()

    def rollAll(self):
        self.roll(range(5))
        
    def roll(self, which):
        """ which is a list of index positions telling the roll method
            which dice to roll """
        for w in which:
            self.dice[w] = randrange(6)+1

    def values(self):
        """ returns the values of the dice
            the slice ':' makes the method return a copy
            instead of the actual object. this prevents
            another part of the program from changing the dice object
        """
        return self.dice[:]

    def score(self):
        #a list of the number of times each number appears in the dice collection
        counts = [0]*7
        for v in self.values():
            counts[v] += 1

        if 5 in counts:
            return 'Five of a Kind', 30
        elif counts.count(1) == 5 and (counts[1]==0 or counts[6]==0):
            return 'Straight', 20
        elif 4 in counts:
            return 'Four of a Kind', 15
        elif (3 in counts) and (2 in counts):
            return 'Full House', 12
        elif 3 in counts:
            return 'Three of a Kind', 8
        elif counts.count(2) == 2:
            return 'Two Pairs', 5
        else:
            return 'garbage hand', 0 
