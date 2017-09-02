#zelle 7.7.1 overtime pay

def main():
    hrs = float(input('hours worked: '))
    rate = float(input('hourly rate: '))

    if hrs > 40:
        pay = 40 * rate + (hrs - 40) * rate * 1.5
    else:
        pay = hrs * rate

    print('total pay: ${0:0.2f}'.format(pay))

main()
    
