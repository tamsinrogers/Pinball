# Program: triangle2.py
#    Program to draw the triangle and calculate its perimeter.
#    Illustrates value returning functions.

import math
from graphicsPlus import *

def main():
    win = GraphWin("Polygon")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    p4 = win.getMouse()
    p4.draw(win)
    p5 = win.getMouse()
    p5.draw(win)
    
    shape = Polygon(p1,p2,p3,p4,p5)
    shape.setOutline("black")
    shape.draw(win)

    win.getMouse()
    win.close()

main()