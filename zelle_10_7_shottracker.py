#zelle 10.7 text example - animated cannonball - shottracker.py

from graphics import *
from zelle_10_7_projectile import Projectile

class ShotTracker():
    """ Keep track of and animate a cannonball """

    def __init__(self, win, height, angle, velocity):
        self.proj = Projectile(height, angle, velocity)
        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill('red')
        self.marker.setOutline('red')
        self.marker.draw(win)

    def update(self, time):
        self.proj.update(time)
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx,dy)

    def getX(self):
        return self.proj.getX()

    def getY(self):
        return self.proj.getY()

    def undraw(self):
        self.marker.undraw()
