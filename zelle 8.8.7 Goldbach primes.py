#zelle 8.8.7 Goldbach conjecture

from math import *

def checkPrime(n):
    i = 2

    result = 'prime'
    
    while i <= sqrt(n):
        if n % i == 0:
            result = 'not prime'
            break
        else:
            i += 1

    return result


def main():
    n = int(input('find Goldbach primes for (even, >2): '))

    if n%2 != 0:
        print('only works for even integers > 2')
        return

    for i in range (2, n+1):
        if checkPrime(i) == 'prime':
            if checkPrime(n - i) == 'prime':
                print('one set of Goldbach primes are ' + str(i) + ' and ' + str(n-i))
                break
    

main()

