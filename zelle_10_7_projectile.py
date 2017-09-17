#zelle 10.7 text example - animated cannonball - projectile.py

from math import sin, cos, radians

class Projectile():
    """ a projectile object given a laungh height, angle, and velocity """

    def __init__(self, height, angle, velocity):
        self.xpos = 0.0
        self.ypos = height
        angleRad = radians(angle)
        self.xvel = velocity * cos(angleRad)
        self.yvel = velocity * sin(angleRad)
    
    def update(self, time):
        self.xpos += self.xvel * time        
        self.ypos += (self.yvel - 0.5*9.8*time) * time
        self.yvel += -9.8 * time

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos
