#zelle 9.1.2 text exercise - racquetball sim

from random import random

def simGame(a, b):

    aScore, bScore = 0, 0
    service = 'a'

    while aScore < 15 and bScore < 15:
        if service == 'a':
            if random() < a:
                aScore += 1
            else:
                service = 'b'
        else:
            if random() < b:
                bScore += 1
            else:
                service = 'a'

    if aScore == 15:
        return 'a'
    else:
        return 'b'
    

def simMatch(a, b, n):

    aWins = 0
    bWins = 0
    
    for i in range(n):
        winner = simGame(a, b)
        if winner == 'a':
            aWins += 1
        else:
            bWins += 1

    return aWins, bWins

def main():

    a = float(input('prob player A wins a serve: '))
    b = float(input('prob player B wins a serve: '))
    n = int(input('games to simulate: '))

    aWins, bWins = simMatch(a, b, n)

    print('\nGames Simulated: ' + str(n) + '\n')
    print('Wins for A: {0:0.0f} ({1:3.1%})'.format(aWins, aWins / n))
    print('Wins for B: {0:0.0f} ({1:3.1%})'.format(bWins, bWins / n))
    

if __name__ == '__main__': main()
