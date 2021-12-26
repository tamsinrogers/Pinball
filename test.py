# Caitrin Eaton
# 01 November 2019
# CS152 Week08:
# Zelle graphics and interactive animation
#
# This program animates a ballistic projectile.

import graphicsPlus as gr
import random
import time


def createWorld(window):
	"""Creates a world of blue sky and green grass. The window must be a
	GraphWin object. Returns a Rectangle that represents the ground."""
	
	# Create a light blue window to represent the sky
	window.setBackground( gr.color_rgb( 150, 200, 255 ) )
	
	# Create a green rectangle to represent the ground
	p1 = gr.Point( 0, window.getHeight() ) 
	p2 = gr.Point( window.getWidth(), window.getHeight()*3//4 )
	grass = gr.Rectangle( p1, p2 )
	grass.setFill( gr.color_rgb(0, 255, 50) )
	grass.draw( window )
	
	# NOTE: GraphWin.getHeight() and .getWidth() are NOT in Zelle's PDF documentation!
	# But I saw it in graphics.py. Always worth poking around in the library :)
	
	return grass
	
	
def createProjectile( window, ground ):
	"""Creates a projectile represented by a Polygon within a Circle that
	is resting on the ground. The ground must be a Rectangle object, and
	window must be a GraphWin object. Returns a list of shapes that 
	represent the projectile."""
		
	# The projectile starts sitting on the ground in the middle of the screen
	radius = 50
	p1 = ground.getP1()
	p2 = ground.getP2()
	xCenter = radius*2								# to the left
	yCenter = min(p1.getY(), p2.getY()) - 3*radius	# above the ground
	pCenter = gr.Point( xCenter, yCenter )
	
	# Draw the projectile's Circle
	circ = gr.Circle( pCenter, radius )
	circ.setFill( "white" )
	circ.draw( window )
	
	# Place a star shape within the Circle
	starScale = 25
	x0 = xCenter - starScale*1.25
	y0 = yCenter - starScale*0.5
	p0 = gr.Point( x0, y0 )
	x1 = x0 + starScale
	y1 = y0
	p1 = gr.Point( x1, y1 )
	x2 = xCenter
	y2 = yCenter - starScale*1.25
	p2 = gr.Point( x2, y2 )
	x3 = xCenter + starScale*0.25
	y3 = y0
	p3 = gr.Point( x3, y3 )
	x4 = x3 + starScale
	y4 = y0
	p4 = gr.Point( x4, y4 )
	x5 = xCenter + starScale*0.5
	y5 = yCenter
	p5 = gr.Point( x5, y5 )
	x6 = xCenter + starScale
	y6 = yCenter + starScale
	p6 = gr.Point( x6, y6 )
	x7 = xCenter
	y7 = y5 + starScale*0.25
	p7 = gr.Point( x7, y7 )
	x8 = xCenter - starScale
	y8 = y6
	p8 = gr.Point( x8, y8 )
	x9 = xCenter - starScale*0.5
	y9 = y5
	p9 = gr.Point( x9, y9 )
	star = gr.Polygon( p0, p1, p2, p3, p4, p5, p6, p7, p8, p9 )
	star.setFill( "yellow" )
	star.draw( window )
	
	return [circ, star]
	
	
def boom(win, ball):
	"""Turns the ball red and displays the message 'BOOM!'. The win must
	be a GraphWin object, and the ball must be a list of 2+ shapes. 
	Returns	2 objects: a copy of ball[1] and the Text "BOOM!". """
	
	# Turn the Circle red
	ball[0].setFill( "red" )
	
	# Make a copy of the Star
	starCopy = ball[1].copy()
	starCopy.draw( win )
		
	# Display the message "BOOM!"
	p = ball[0].getCenter()
	x = p.getX() + 25
	y = p.getY() - 225
	message = gr.Text( gr.Point(x,y), "BOOM!" )
	message.setSize( 75 )
	message.setFace( "helvetica" )
	message.draw( win )
	
	return (starCopy, message)

def animateProjectile():
	"""Animates a ballistic projectile."""
	
	# Create the window in which the animation will be displayed
	win = gr.GraphWin("Ball Simulation", 700, 400, False)
	
	# Draw the world (sky and grass) and the projectile
	ground = createWorld( win )
	p1 = ground.getP1()
	p2 = ground.getP2()
	groundLevel = min(p1.getY(), p2.getY())	# top of the ground
	win.update()
	win.getMouse()
	
	# Draw the projectile
	ball = createProjectile( win, ground )
	win.update()
	win.getMouse()
	
	# Velocity, acceleration, and pixel:meter scale
	vx = 10			# meters / second
	vy = 0			# meters / second
	g = -9.80665	# meters / second**2
	dt = 0.01		# seconds / frame
	ppm = 10		# pixels / meter
	t = 0			# current time, in seconds
	
	# Animate!
	c = ball[0].getCenter()	# center Point of the projectile
	while 0 < c.getX() and c.getX() < win.getWidth():
		
		# Calculate the ball's change in position, 
		# making sure it doesn't penetrate the ground
		dxm = vx * dt
		dxp = dxm * ppm
		dym = vy * dt  +  0.5 * g * dt**2
		vy = vy + g * dt
		dyp = -dym * ppm
		if c.getY() + ball[0].getRadius() + dyp > groundLevel:
			dyp = groundLevel - c.getY() - ball[0].getRadius()
		
		# Move the ball
		for shape in ball:
			shape.move( dxp, dyp )
		c = ball[0].getCenter()
			
		# Refresh the window
		win.update()
		time.sleep( dt )
		t += dt
	
	# Close when a human clicks in the window
	win.getMouse()
	win.close()
	
if __name__ == "__main__":
	animateProjectile()