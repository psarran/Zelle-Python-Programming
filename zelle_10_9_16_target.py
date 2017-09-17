#zelle_10_9.16 cannonball target

from graphics import *
from random import randrange

class Target():
    """ cannonball target """

    def __init__(self, width, height, xlow, xhigh, ylow, yhigh, win):

        self.targetY = randrange(ylow, yhigh)
        self.targetX = randrange(xlow, xhigh)
        self.targetHeight = height
        self.targetWidth = width

        pt1 = Point(self.targetX, self.targetY)
        pt2 = Point(self.targetX + self.targetWidth, self.targetY + self.targetHeight)
        self.target = Rectangle(pt1, pt2)
        self.target.draw(win)

    def checkHit(self, pt):
        yhit = self.targetY < pt.getY() < self.targetY+self.targetHeight
        xhit = self.targetX < pt.getX() < self.targetX+self.targetWidth
        return yhit and xhit

    def setOutline(self, color):
        self.target.setOutline(color)
