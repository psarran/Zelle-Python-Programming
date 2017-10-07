#zelle 12.2 racquetball objects

from random import random

class RGame():

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.winpt = 15
        self.shutoutpt = 7
        self.winner = ''
        self.shutout = ''

    def play(self):
        aScore, bScore = 0, 0
        service = 'a'
        while True:
            if (    aScore==self.winpt
                or  bScore==self.winpt
                or (aScore==self.shutoutpt and bScore==0)
                or (aScore==0 and bScore==self.shutoutpt)
               ):
                break                                    
            if service == 'a':
                if random() < self.a:
                    aScore += 1
                else:
                    service = 'b'
            else:
                if random() < self.b:
                    bScore += 1
                else:
                    service = 'a'

        if aScore==self.winpt or aScore==self.shutoutpt:
            self.winner='a'
        if bScore==self.winpt or bScore==self.shutoutpt:
            self.winner='b'
        if aScore==self.shutoutpt:
            self.shutout='a'
        if bScore==self.shutoutpt:
            self.shutout='b'

    def getWinner(self):
        return self.winner

    def getShutout(self):
        return self.shutout

class SimStats():

    def __init__(self):
        self.aWins = 0
        self.bWins = 0
        self.aShutouts = 0
        self.bShutouts = 0
        self.n = 0

    def update(self, game):
        if game.getWinner() == 'a':
            self.aWins += 1
            self.n += 1
        elif game.getWinner() == 'b':
            self.bWins += 1
            self.n += 1
        if game.getShutout() == 'a':
            self.aShutouts += 1
        elif game.getShutout() == 'b':
            self.bShutouts += 1

    def printResults(self):
        print('\nGames Simulated: ' + str(self.n) + '\n')
        print('Wins for A: {0:0.0f} ({1:3.1%})'.format(self.aWins, self.aWins / self.n))
        print('Wins for B: {0:0.0f} ({1:3.1%})'.format(self.bWins, self.bWins / self.n))
        print('Shutouts for A: {0:0.0f}'.format(self.aShutouts))
        print('Shutouts for B: {0:0.0f}'.format(self.bShutouts))
    
