#zelle 6.9.16 draw face

from graphics import *
import math

def drawFace(center, size, win):
    face = Circle(center, size)
    face.setFill('yellow')
    face.draw(win)
    eyeUp = size / 3
    eyeOver = size / 2.5
    eyeSize = size / 4
    faceX = center.getX()
    faceY = center.getY()

    leftEye = Circle(Point(faceX - eyeOver,faceY - eyeUp), eyeSize)
    leftEye.setFill('black')
    leftEye.draw(win)

    rightEye = Circle(Point(faceX + eyeOver,faceY - eyeUp), eyeSize)
    rightEye.setFill('black')
    rightEye.draw(win)

    mouth = Line(Point(faceX - size/3, faceY + size/3), Point(faceX + size/3, faceY + size/2.5))
    mouth.draw(win)


def main():
    fname = input('enter filename: ')
    myImage = Image(Point(0,0), fname)

    wWidth = myImage.getWidth()
    wHeight = myImage.getHeight()

    win = GraphWin('draw face', wWidth, wHeight)
    myImage.move(wWidth/2, wHeight/2)
    myImage.draw(win)
    

    faceCount = int(input('how many faces? '))

    for i in range(faceCount):
        print('click center of face')
        p1 = win.getMouse()
        print('click edge of face')
        p2 = win.getMouse()
        r = math.sqrt( (p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
        drawFace(p1, r, win)


main()
