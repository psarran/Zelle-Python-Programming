#zelle 7.5.1 exercise - max of three

def main():
    x1, x2, x3 = eval(input('input three #s: '))

    if x1 > x2:
        if x1 > x3:
            maxval = x1
        else:
            maxval = x3
    else:
        if x2 > x3:
            maxval = x2
        else:
            maxval = x3
        
    print('largest value is: ', maxval)

#main()

def main2():
    
    x1, x2, x3 = eval(input('input three #s: '))

    if x1 >= x2 and x1 >= x3:
        maxval = x1
    elif x2 >= x1 and x2 >= x3:
        maxval = x2
    else:
        maxval = x3

    print('largest value is: ', maxval)

#main2()

def main3():

        
    x1, x2, x3 = eval(input('input three #s: '))

    if x1 >= x2:
        maxval = x1
    else:
        maxval = x2

    if x3 >= maxval:
        maxval = x3

    print('largest value is: ', maxval)

main3()

