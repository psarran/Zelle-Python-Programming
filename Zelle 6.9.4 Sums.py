#Zelle 6.9.4 Sums

def sumN(n):
    out = 0
    for i in range(n+1):
        out += i
    return out

def sumNCubes(n):
    out = 0
    for i in range(n+1):
        out += i ** 3
    return out

def main():
    inputN = int(input('what n? '))
    print('sum of first n natural numbers: ' + str(sumN(inputN)))
    print('sum of cubes of first n natural numbers: ' + str(sumNCubes(inputN)))

main()
