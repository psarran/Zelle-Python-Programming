#zelle 8.6 text example - event loop

from graphics import *

def setup():
    win = GraphWin('event loop', 500, 500)
    print('type first letter of color to change color of window, type \'q\' to quit')
    print('click in window to enter text')
    print('\n')
    print('colors choices:')
    print('b - blue')
    print('g - green')
    print('r - red')
    print('o - orange')
    print('\n')

    key = ''

    colorKeys = ['b', 'g', 'r', 'o']
    colors = ['blue', 'green', 'red', 'orange']

    return win, key, colorKeys, colors
    
def handleKey(key, win, colorKeys, colors):
    try:
        color = colors[colorKeys.index(key)]
        win.setBackground(color)
    except:
        pass
    
def handleMouseClick(pt, win):
    entry = Entry(pt, 10)
    entry.draw(win)
    
    while True:
        key = win.checkKey()
        if key == 'Return': break
        if key == 'Escape': break

    win.checkMouse()
    entry.undraw()
    
    if key == 'Escape': return
    
    text = entry.getText()
    Text(pt, text).draw(win)

def main():
    win, key, colorKeys, colors = setup()
    
    while True:
        key = win.checkKey()
        if key == 'q': break
        if key:
            handleKey(key, win, colorKeys, colors)

        click = win.checkMouse()
        if click:
            handleMouseClick(click, win)          
    
    win.close()

main()
