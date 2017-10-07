#zelle 12.2 text exercise - racquetball sim

from random import random
from zelle_12_2_racquetball_objects import RGame, SimStats

def getInputs():
    a = float(input('prob player A wins a serve: '))
    b = float(input('prob player B wins a serve: '))
    n = int(input('games to simulate: '))

    return a, b, n


def main():
    a, b, n = getInputs()
    stats = SimStats()
    for i in range(n):
        aGame = RGame(a, b)
        aGame.play()
        stats.update(aGame)
    stats.printResults()
    

if __name__ == '__main__': main()
