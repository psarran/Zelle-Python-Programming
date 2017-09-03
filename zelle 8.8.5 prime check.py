#zelle 8.8.5 prime check

from math import *

def main():
    n = int(input('integer > 2: '))

    i = 2

    result = 'prime'
    
    while i <= sqrt(n):
        if n % i == 0:
            result = 'not prime'
            break
        else:
            i += 1

    print(result)
    

main()
