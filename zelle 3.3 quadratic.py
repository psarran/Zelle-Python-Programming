# zelle 3.3 quadratic

import math

def main():
    print('returns the two roots of a quadratic eq')
    print()

    a = float(input('a= '))
    b = float(input('b= '))
    c = float(input('c= '))

    discRoot = math.sqrt(b**2 - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print('the two roots are:', root1, root2)

main()
