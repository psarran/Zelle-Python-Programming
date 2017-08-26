# zelle 5.11.3

import math

def main():
    grades = ['F', 'D', 'C', 'B', 'A', 'A']
    score = int(input('score: '))
    scoreAdj = max(0,math.floor(score / 10)-5)
    print(grades[scoreAdj])

main()

