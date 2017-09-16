#zelle 10.6.1 text example - dice - button.py

from graphics import *

class Button():
    """ Creates a Button object with methods activate(), deactivate(),
        and clicked(pt) """

    def __init__(self, win, center, width, height, label):
        """ Create button object which consists of a Rectangle centered at 'center'
            with a Text object with text 'label' """
        w, h = width/2, height/2
        x, y = center.getX(), center.getY()
        self.xmin, self.ymin = x-w, y-h
        self.xmax, self.ymax = x+w, y+h

        pt1 = Point(self.xmin, self.ymin)
        pt2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(pt1, pt2)

        self.label = Text(center,label)
        self.label.setTextColor('lightgrey')

        self.rect.draw(win)
        self.label.draw(win)
        self.deactivate()

    def activate(self):
        """ sets to active / available to be clicked """
        self.label.setTextColor('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """ sets to inactive / unavailable to be clicked """
        self.label.setTextColor('darkgrey')
        self.rect.setWidth(1)
        self.active = False
        
    def clicked(self, pt):
        """ if button is active this will determine if there was a click
            (pt) within the button """
        return (self.active and self.xmin <= pt.getX() <= self.xmax
                            and self.ymin <= pt.getY() <= self.ymax)

    def getLabel(self):
        """ returns the label text """
        return self.label.getText()
