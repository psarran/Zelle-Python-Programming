#zelle 8.8.6 find primes

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
    n = int(input('find all primes less than: '))

    primes = []

    for j in range(3, n+1):
        if checkPrime(j) == 'prime': primes.append(j)

    print(primes)
    

main()
