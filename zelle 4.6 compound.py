# zelle 4.6 bar graph

from graphics import *

def main():
    print('bar graph of 10 yr investment')
    print()

    princ = float(input('orig principal = '))
    rate = float(input('rate = '))

    win = GraphWin("Investment Growth Chart",320,240)
    Text(Point(20,230),' 0.0K').draw(win)
    Text(Point(20,180),' 2.5K').draw(win)
    Text(Point(20,130),' 5.0K').draw(win)
    Text(Point(20,80),' 7.5K').draw(win)
    Text(Point(20,30),'10.0K').draw(win)

    for i in range(11):
        amt = princ * ((1+rate) ** i)
        bar = Rectangle(Point(40+25*i, 230), Point(65+25*i, 230-amt*0.02))
        bar.draw(win)
        bar.setFill('green')
        bar.setWidth(2)
        
    input('press enter')

main()
