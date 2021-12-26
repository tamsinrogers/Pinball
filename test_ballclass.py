# Bruce Maxwell
# Fall 2015
# CS 151S Project 9
#
# ball class test
#
# modified slightly by Eric Aaron for CS 152, Spring '19
# slightly updated by Bruce Maxwell for CS 152, Fall 2019
#     simplified the constructor call to just the win variable

import graphicsPlus as gr
import physics_objects as pho
import collision as coll
import time

# create two balls heading towards one another
def main():
    win = gr.GraphWin( 'balls colliding', 500, 500, False )

    ball1 = pho.Ball( win )
    ball2 = pho.Ball( win )
    
    triangle = pho.Triangle(win, color=(0,0,128))
    block = pho.Block(win, color=(0,0,128))
    
    ball1.setPosition( 20, 20 )
    ball2.setPosition( 30, 20 )
    triangle.setPosition(10, 20)
    block.setPosition(40, 20)

    # set up velocity and acceleration so they collide
    ball1.setVelocity( 20, 20 )
    ball2.setVelocity( -20, 20 )
    ball1.setAcceleration( 0, -20 )
    ball2.setAcceleration( 0, -20 )
    ball1.draw()
    ball2.draw()
    
    triangle.draw()
    block.draw()

    # loop for some time and check for collisions
    dt = 0.01
    for frame in range(120):
        if not coll.collision_ball_ball( ball1, ball2, dt ):
            ball1.update(dt)

        if not coll.collision_ball_ball( ball2, ball1, dt ):
            ball2.update(dt)
        
        if frame % 10 == 0:
            win.update()

        time.sleep(0.5*dt)
        if win.checkMouse() != None:
            break
            
    shape = [triangle, block]
    for item in shape:
    	coll.collision(item, block, dt)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()