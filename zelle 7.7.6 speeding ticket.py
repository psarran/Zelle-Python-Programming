#zelle 7.7.6 speeding ticket

def main():
    limit = float(input('speed limit: '))
    speed = float(input('speed: '))
    
    if speed <= limit:
        print('y\'all good')
    elif speed <= 90:
        fine = 50 + 5 * (speed - limit)
        print('fine: ${0:0.2f}'.format(fine))
    else:
        fine = 50 + 5 * (speed - limit) + 200
        print('fine: ${0:0.2f}'.format(fine))

main()
