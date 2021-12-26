# Tamsin Rogers
# November 12, 2019
# CS 152 
# Project 9: Pinball
# run this program from the Terminal by entering "python3 pinball.py"
# this program creates a pinball simulation using ball and block objects

#import the physics_objects file, collision file, and graphicsPlus package
import physics_objects as pho
import collision
import graphicsPlus as gr
import random
import time
import math
from graphicsPlus import *

"""This function creates all of the obstacles in the scene and puts them into a list called theshapes."""
def buildObstacles(win):
    #the walls
    bottomwall = pho.Block(win)
    leftwall = pho.Block(win)
    topwall = pho.Block(win)
    rightwall = pho.Block(win)
    rightwall = pho.Block(win)
    rightwall.setPosition(50,0)
    rightwall.setHeight(100)
    rightwall.setWidth(1.5)
    rightwall.setColor((0,0,0))
    leftwall = pho.Block(win)
    leftwall.setPosition(0,50)
    leftwall.setHeight(100)
    leftwall.setWidth(1.5)
    leftwall.setColor((0,0,0))
    topwall = pho.Block(win)
    topwall.setPosition(0,50)
    bottomwall = pho.Block(win)
    bottomwall.setPosition(10,0)
    wall = [leftwall, rightwall, topwall, bottomwall]
    #the blocks
    block1 = pho.Block(win)
    block1.setHeight(1.5)
    block1.setWidth(1.5)
    block1.setPosition(10,10)
    block1.setColor((3,207,252))
    block1.setElasticity(.3)
    block2 = pho.Block(win)
    block2.setHeight(1.5)
    block2.setWidth(1.5)
    block2.setPosition(20,20)
    block2.setColor((84,221,255))
    block2.setElasticity(.3)
    block3 = pho.Block(win)
    block3.setHeight(1.5)
    block3.setWidth(1.5)
    block3.setPosition(30,30)
    block3.setColor((158,236,255))
    block3.setElasticity(.3)
    block4 = pho.Block(win)
    block4.setHeight(1.5)
    block4.setWidth(1.5)
    block4.setPosition(40,40)
    block4.setColor((222,248,255))
    block3.setElasticity(.3)
    blockobstacles = [block1, block2, block3, block4]
    #the triangles
    triangle1 = pho.Triangle(win)
    triangle1.setPosition(15,7)
    triangle1.setColor((124,54,255))
    triangle2 = pho.Triangle(win)
    triangle2.setPosition(30,40)
    triangle2.setColor((152,97,255))
    triangle3 = pho.Triangle(win)
    triangle3.setPosition(30,10)
    triangle3.setColor((192,158,255))
    triangle4 = pho.Triangle(win)
    triangle4.setPosition(7,40)
    triangle4.setColor((224,207,255))
    triangleobstacles = [triangle1, triangle2, triangle3, triangle4]
    #the balls
    ball1 = pho.Ball(win)
    ball1.setPosition(15,30)
    ball1.setRadius(3)
    ball1.setColor((255,207,207))
    ball1.setElasticity(3)
    ball2 = pho.Ball(win)
    ball2.setPosition(30,15)
    ball2.setRadius(1.5)
    ball2.setColor((255,130,130))
    ball1.setElasticity(1)
    
    newshape = pho.Newshape(win)
    
    # Each obstacle should be a Thing (e.g. Ball, Block, other)
    # You might want to give one or more the obstacles an elasticity > 1
    # Return the list of Things
    thewall = [topwall, bottomwall, leftwall, rightwall, block1, block2, block3, block4, triangle1, triangle2, triangle3, triangle4, ball1, ball2]
    return thewall

"""The main function creates a new graphics window, calls the previously defined buildObstacles 
function, and stores the return list in the shapes variable.  It then loops over the shapes 
list to draw the objects in the window and sets up timing and frames.  This function also 
contains logistics for determining if a ball has moved outside of the window or collided 
with another object. """
def main():

    # create a GraphWin
    win = gr.GraphWin( 'pinball', 500, 500, False )
    win.setBackground("white")                                  #set the color of the background of the window to white
    
    # call buildObstacles, storing the return list in a variable (e.g. shapes)
    shapes = buildObstacles(win)
    # loop over the shapes list and have each Thing call its draw method
    for i in shapes:
        i.draw()
    # assign to dt the value 0.02
    dt = 0.02
    # assign to frame the value 0
    frame = 0
    
    """# create a ball, give it an initial velocity and acceleration, and draw it
    ball = pho.Ball(win)
    ball.setPosition( 20, 20 )
    ball.setVelocity( 20, 20 )
    ball.setAcceleration( 0, -20 )
    ball.setElasticity(2)
    ball.setColor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    ball.draw()"""
    
    newshape = pho.Newshape(win)
    newshape.setPosition( 20, 20 )
    newshape.setVelocity( 20, 20 )
    newshape.setAcceleration( 0, -20 )
    newshape.setElasticity(2)
    newshape.setColor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    newshape.draw()
    

    # start an infinite loop
    while True:
        newshape.setColor((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        # if frame modulo 10 is equal to 0
        if frame%10 == 0:
            # call win.update()
            win.update()

        # using checKey, if the user typed a 'q' then break
        key = win.checkKey()
        if key == "q":
            break
        # if the ball is out of bounds, re-launch it
        if newshape.getPosition()[0] > win.getWidth() or newshape.getPosition()[1] < 0: #if the ball is outside the window
            newshape.setPosition(25, 25)                                            #reposition the ball to the center of the window
            newshape.setVelocity(random.randint(0,10), random.randint(0,10))        #give the ball a random velocity
            newshape.update(.01)
        # assign to collided the value False
        collided = False
        # for each item in the shapes list
        for i in shapes:
            # if the result of calling the collision function with the ball and the item is True
            if collision.collision(newshape, i, .01) == True:
                # set collided to True
                collided = True

        # if collided is equal to False
        if collided == False:
            # call the update method of the ball with dt as the time step
            newshape.update(dt)

        # increment frame
        frame = frame + 1

    # close the window
    win.getMouse()
    win.close()       

if __name__ == "__main__":
    main()