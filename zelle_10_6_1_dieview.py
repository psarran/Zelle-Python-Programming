#zelle 10.6.1 text example - dice - dieview.py

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
        self.pip1 = self.__makePip(cx-offset, cy-offset)
        self.pip2 = self.__makePip(cx-offset, cy)
        self.pip3 = self.__makePip(cx-offset, cy+offset)
        self.pip4 = self.__makePip(cx+offset, cy-offset)
        self.pip5 = self.__makePip(cx+offset, cy)
        self.pip6 = self.__makePip(cx+offset, cy+offset)
        self.pip7 = self.__makePip(cx, cy)

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
        #turn off all pips
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        #fill in appropriate pips
        if v == 1:
            self.pip7.setFill(self.foreground)
        elif v == 2:
            self.pip1.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
        elif v == 3:
            self.pip1.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif v == 4:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
        elif v == 5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif v == 6:
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip6.setFill(self.foreground)

            
