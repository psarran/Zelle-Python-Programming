#zelle 8.8.4 syracuse sequence

def main():
    n = int(input('starting integer: '))
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        seq.append(int(n))

    print(seq)

main()
