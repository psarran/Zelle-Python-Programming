#zelle 10.6.1 text example - dice - dieview.py
#updated for chapter 12.3

from graphics import *

class DieView():
    """ Controls the display and updating of a Die object """

    def __init__(self, win, center, size):
        """ Draw the die centered at 'center' (a Point) with length 'size' """
        self.win = win
        self.background = 'white' #color of die
        self.foreground = 'black' #color of pips
        self.psize = 0.1 * size   #radius of each pip
        cx, cy = center.getX(), center.getY()
        offset = 0.6 * size/2


        #make the outline
        p1, p2 = Point(cx-size/2, cy-size/2), Point(cx+size/2, cy+size/2)
        rect = Rectangle(p1, p2)
        rect.setOutline(self.foreground)
        rect.setFill(self.background)
        rect.draw(win)

        #make the pips
        self.pips = [self.__makePip(cx-offset, cy-offset),
                     self.__makePip(cx-offset, cy)       ,
                     self.__makePip(cx-offset, cy+offset),
                     self.__makePip(cx+offset, cy-offset),
                     self.__makePip(cx+offset, cy)       ,
                     self.__makePip(cx+offset, cy+offset),
                     self.__makePip(cx, cy)
                    ]
        self.fillList = [ [], [7], [1, 6], [1, 6, 7], [1, 3, 4, 6],
                          [1, 3, 4, 6, 7], [1, 2, 3, 4, 5, 6] ]

        #set initial value
        self.setValue(1)

    def __makePip(self, x, y):
        """ Helper method to draw a pip at (x, y) """
        pip = Circle( Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, v):
        self.value = v
        
        #turn off all pips
        for p in self.pips:
            p.setFill(self.background)

        #fill in appropriate pips
        for p in self.fillList[v]:
            self.pips[p-1].setFill(self.foreground)
            
    def setColor(self, color):
        self.foreground = color
        self.setValue(self.value)
