import graphicsPlus as gr
import random
import math
from graphicsPlus import *

#the parent class for simulated objects
class Thing:
    """This function initializes the attributes of objects in the Thing class.  Win and the_type are the required parameters."""
    def __init__(self, win, the_type):
        self.win = win              #the GraphWin window for drawing
        self.the_type = "type"      #the type of thing being created
        self.mass = 0               #A scalar value indicating the mass of the object.
        self.position = [0,0]       #A 2-element list indicating the current position of the object.
        self.velocity = [0,0]       #A 2-element list indicating the current velocity of the object.
        self.acceleration = [0,0]   #A 2-element list indicating acceleration acting on the object.
        self.elasticity = .5         #The amount of energy retained after a collision.
        self.scale = 10             #The scale factor between the simulation space and pixels. Default to 10.
        self.vis = []               #An empty list that will hold Zelle graphics.
        self.color = (0,0,0)       #An (r, g, b) tuple. A good default value is black (0, 0, 0).
        self.drawn = False          #A boolean indicating if the shape has been drawn, initially False.
    #GET METHODS
    """This function takes the argument self and returns the type of the object as a string."""
    def getType(self):
        return "thing"
    """This function takes the argument self and returns the mass of the object."""
    def getMass(self):
        return self.mass
    """This function takes the argument self and returns a 2 element tuple with the x,y position of the ball object."""
    def getPosition(self):          
        return self.position[:]
    """This function takes the argument self and returns a 2 element tuple with the x and y velocities."""
    def getVelocity(self):          
        return self.velocity[:]
    """This function takes the argument self and returns a 2 element tuple with the x and y accelerations.""" 
    def getAcceleration(self):      
        return self.acceleration[:]
    """This function takes the argument self and returns the elasticity value, or the amount of energy retained after a collision, of the object."""
    def getElasticity(self):
        return self.elasticity
    """This function takes the argument self and returns the scale factor between the simulation space and pixels."""
    def getScale(self):
        return self.scale
    """This function takes the argument self and returns an (r, g, b) tuple that sets the color of the object."""
    def getColor(self):
        return self.color
    """This function takes the argument self and returns a boolean indicating if the referenced shape has been drawn."""
    def getDrawn(self):
        return self.drawn
    #DRAW/UNDRAW METHODS
    """This function takes the argument self and loops through the vis list to draw the object in the window."""
    def draw(self):
        for i in self.vis:
            i.draw(self.win)
    """This function takes the argument self and loops through the vis list to undraw the object in the window."""
    def undraw(self):
        for i in self.vis:
            i.undraw()
    #SET METHODS
    """This function takes self and m as arguments and sets the mass of the object."""
    def setMass(self, m):
        self.mass = m
    """This function sets the x,y velocity of the thing object.   The vx and vy variables 
    are the new x,y values.  The x coordinate of v is assigned to the x coordinate in self.velocity, 
    and the y coordinate of v is assigned to the y coordinate in self.velocity."""     
    def setVelocity(self, vx, vy):      # vx and vy are the new x and y velocities
        self.velocity[0] = vx
        self.velocity[1] = vy
    """This function sets the x,y acceleration of the thing object.   The ax and ay variables 
    are the new x,y values.  The x coordinate of a is assigned to the x coordinate in self.acceleration, 
    and the y coordinate of a is assigned to the y coordinate in self.acceleration."""  
    def setAcceleration(self, ax, ay):  # ax and ay are new x and y accelerations.
        self.acceleration[0] = ax
        self.acceleration[1] = ay
    """This function sets the amount of energy retained by an object after a collision 
    (elasticity) to the variable e."""
    def setElasticity(self, e):
        self.elasticity = e
    """This function sets the x,y position of the Thing object.  This is done by calculating 
    the difference between the new position (px, py) and the current position (self.position[0], self.position[1]).  
    These values are then set into dx, dy, and the ball's position fields are updated with 
    the new positions.  The setPosition function is finalized by multiplying dx by self.scale 
    and dy by -self.scale, and moving the vis list items by dx and dy within a for loop.'"""       
    def setPosition(self, px, py):
        self.position[0] = px           # assign to the x coordinate in self.pos the x coordinate of p
        self.position[1] = py           # assign to the y coordinate in self.pos the y coordinate of p
        c = self.vis[0].getCenter()
        dx = (self.scale*px)-(c.getX())
        dy = (self.win.getHeight()-(self.scale*py)-(c.getY()))
        for i in self.vis:
            i.move(dx, dy)
    """This function sets the color field of the shape to c.  If c is not None, the function 
    loops over the self.vis list and sets the fill color of the referenced shape object to 
    the appropriate color using rgb values."""
    def setColor(self, c):
        self.color = c
        if c != None:
            for i in self.vis:
                thecolor = gr.color_rgb(self.color[0], self.color[1], self.color[2])
                i.setFill(thecolor)
    """This function adjusts the position, velocity, and vis values of the thing object through 
    dependence on its current acceleration and force values.  It takes one argument (dt), 
    which is the time step that indicates how much time to run the simulation for."""
    def update(self, dt):
        # update the x position using x_new = x_old + x_vel*dt + 0.5*x_acc * dt*dt
        self.position[0] = self.position[0] + self.velocity[0]*dt + 0.5*self.acceleration[0] * dt*dt
        # update the y position using y_new = y_old + y_vel*dt + 0.5*y_acc * dt*dt 
        self.position[1] = self.position[1] + self.velocity[1]*dt + 0.5*self.acceleration[1] * dt*dt
        # assign to dx the change in the x position times the scale factor (self.scale)
        dx = (self.velocity[0]*dt + 0.5 * self.acceleration[0] * dt * dt)*self.scale
       # assign to dy the negative of the change in the y position times the scale factor (self.scale)
        dy = -(self.velocity[1]*dt + 0.5 * self.acceleration[1] * dt * dt)*self.scale
        # for each item in self.vis
        for i in self.vis:
            # call the move method of the graphics object with dx and dy as arguments.
            i.move(dx, dy)

        # update the x velocity by adding the acceleration times dt to its old value
        self.velocity[0] = self.velocity[0]+(self.acceleration[0]*dt)
        # update the y velocity by adding the acceleration times dt to its old value
        self.velocity[1] = self.velocity[1]+(self.acceleration[1]*dt)
    
    
class Ball(Thing):
    """This function initializes the attributes of objects in the Ball class, which are inherited from the Thing class."""
    def __init__(self, win, x0=0, y0=0, radius=1, color=(0,0,0), type = "ball"):
        Thing.__init__(self, win, "ball")
        self.win = win
        self.radius = radius
        self.position = [x0, y0]
        self.color = color
        self.refresh()
        self.setColor(self.color)
    def getType(self):
        return "ball"
    """This function assigns drawn to the value of self.drawn.  Then, if the shape is draw, 
    it undraws it using self.undraw.  The function then defines the self.vis list of graphics 
    objects using the current position, radius, and window values, and if the object is drawn, 
    draws it."""
    def refresh(self):
        drawn = self.drawn
        if drawn:
            self.undraw()
        self.vis = [ gr.Circle( gr.Point(self.position[0]*self.scale, self.win.getHeight()-self.position[1]*self.scale), self.radius * self.scale ) ]
        if drawn:
            self.draw()
    """This function returns the radius of the ball object."""
    def getRadius(self):
        return self.radius
    """This function assigns r to the radius field and then calls self.refresh()."""
    def setRadius(self,r):
        self.radius = r
        self.refresh()
        
class Block(Thing):
    """This function initializes the attributes of objects in the Block class, which are inherited from the Thing class."""
    def __init__ (self, win, dx=100, dy=2, color=(0,0,0), type = "block"):
        Thing.__init__(self, win, "block")
        self.win = win
        self.position = [0, 0]        
        self.color = color
        self.width = dx
        self.height = dy
        self.reshape()  #set up the vis list
        self.setColor((0,0,0))    #set the color
    def getType(self):
        return "block"
    """This function undraws the block's graphics objects if they are drawn and defines the 
    self.vis list of graphics objects using the appropriate fields.  It then draws the graphics 
    objects for block if they are drawn."""
    def reshape(self):
        if self.drawn:
            self.undraw()
        self.vis = [gr.Rectangle(gr.Point((self.position[0]-self.width/2)*self.scale, (self.position[1]-self.height/2)*self.scale), gr.Point((self.position[0]+self.width/2)*self.scale, (self.position[1]+self.height/2)*self.scale))]
        if self.drawn:
            self.draw()
    """This function returns the width of the block object."""
    def getWidth(self):
        return self.width
    """This function returns the height of the block object."""
    def getHeight(self):
        return self.height
    """This function resets the width of the block object using the dx variable and the reshape function."""
    def setWidth(self, dx):
        self.width = dx
        self.reshape()
    """This function resets the height of the block object using the dy variable and the reshape function."""
    def setHeight(self, dy):
        self.height = dy
        self.reshape()

class Triangle(Thing):
    """This function initializes the attributes of objects in the Triangle class, treating the object like a Block object, whose attributes are inherited from the Thing class."""
    def __init__ (self, win, length = 10, dx=5, dy=5, color=(0,0,128), type = "triangle"):
        #print("this is the triangle init")
        self.length = length
        Thing.__init__(self, win, "triangle")
        #print("length", self.length)
        self.win = win
        self.position = [0, 0]        
        self.color = color
        self.setColor(self.color)
        self.width = dx
        self.height = dy
        self.reshape()
        self.setColor((255,0,0))
    def getType(self):
        return "triangle"
    """This function returns the length of the triangle object, treating it like block object."""        
    def getLength(self):
        return self.length
    """This function returns the width of the triangle object, treating it like block object."""
    def getWidth(self):
        return self.width
    """This function returns the height of the triangle object, treating it like a block object."""
    def getHeight(self):
        return self.height
    """This function resets the width of the triangle object by treating it as a block using the dx variable and the reshape function."""
    def setWidth(self, dx):
        self.width = dx
        self.reshape()
    """This function resets the height of the triangle object by treating it as a block using the dy variable and the reshape function."""
    def setHeight(self, dy):
        self.height = dy
        self.reshape()
    """This function resets the position of the triangle object."""   
    def setPosition(self, px, py):
        self.position[0] = px
        self.position[1] = py
        pt = self.vis[0].getPoints()[0]
        dx = px*self.scale - pt.getX()
        dy = (self.win.getHeight() - (py*self.scale) - pt.getY())
        for i in self.vis:
            i.move(dx,dy)  
    """This function returns the position of the triangle object as the center of it."""   
    def getCenter(self):
        return self.position
    """This function undraws the triangle's graphics objects if they are drawn and defines the 
    self.vis list of graphics objects using the appropriate fields.  It then draws the graphics 
    objects for triangle if they are drawn.  The v1, v2, and v3 variables represent the vertices 
    of the triangle object."""
    def reshape(self):
        if self.drawn:
            self.undraw()
        x0 = self.position[0]
        y0 = self.position[1]
        v1 = gr.Point(x0 * self.scale, (self.win.getHeight() - (self.scale) * y0 + ((self.length * 3 ** (1/2)) / 4 )))  
        v2 = gr.Point((x0 - self.length/2) * self.scale, (self.win.getHeight() - (self.scale)*(y0 - (self.length * (3** (1/2))/4))))
        v3 = gr.Point((x0 + self.length/2) * self.scale, (self.win.getHeight() - (self.scale)*(y0 - (self.length * (3** (1/2))/4))))
        vertices = [v1, v2, v3]
        self.vis = [gr.Polygon([v1, v2, v3])]
        if self.drawn:
            self.draw()
            
class Newshape(Thing):
    """This function initializes the attributes of objects in the Newshape class, which are inherited from the Thing class."""
    def __init__(self, win, x0=4, y0=2, dx=4, dy=2, radius=4, color=(0,0,0), type = "newshape"):
        Thing.__init__(self, win, "newshape")
        self.win = win
        self.radius = radius
        self.position = [x0, y0]
        self.color = color
        self.width = dx
        self.height = dy
        self.refresh()
        self.setColor(self.color)
    def getType(self):
        return "newshape"
    """This function assigns drawn to the value of self.drawn.  Then, if the shape is draw, 
    it undraws it using self.undraw.  The function then defines the self.vis list of graphics 
    objects using the current position, radius, and window values, and if the object is drawn, 
    draws it."""
    def refresh(self):
        drawn = self.drawn
        if drawn:
            self.undraw()
        oval = gr.Oval(gr.Point((self.position[0]-self.width/2)*(self.scale/2), (self.position[1]-self.height/2)*(self.scale/3)), gr.Point((self.position[0]+self.width/2)*(self.scale/3), (self.position[1]+self.height/2)*(self.scale/2)))
        rectangle = gr.Rectangle(gr.Point((self.position[0]-self.width/2)*self.scale, (self.position[1]-self.height/2)*self.scale), gr.Point((self.position[0]+self.width/2)*self.scale, (self.position[1]+self.height/2)*self.scale))
        self.vis = [oval, rectangle]

        if drawn:
            self.draw()
    """This function returns the radius of the ball object."""
    def getRadius(self):
        return self.radius
    """This function assigns r to the radius field and then calls self.refresh()."""
    def setRadius(self,r):
        self.radius = r
        self.refresh()