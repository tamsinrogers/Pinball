import graphicsPlus as gr
import random

class Ball:

    """This function initializes the attributes of the ball object.  Self and win are the 
    only non optional arguments."""
    def __init__(self, win, mass=1, radius=1):
        
        self.mass = mass
        self.radius = radius
        self.position = [0,0]
        self.velocity = [0,0]
        self.acceleration = [0,0]
        self.win = win
        self.scale = 10
        self.vis = [ gr.Circle( gr.Point(self.position[0]*self.scale, win.getHeight()-self.position[1]*self.scale), self.radius * self.scale ) ]

    """This function draws the ball object in the window."""
    def draw(self):
        for i in self.vis:
            i.draw(self.win)
    
    """"This function undraws the ball object in the window."""
    def undraw(self):
        for i in self.vis:
            i.undraw()
    
    """This function returns the height of the window."""
    def getHeight(self):
        return self.height
    
    """This function returns the width of the window."""
    def getWidth(self):
        return self.width
    
    """This function returns the mass of the ball object."""
    def getMass(self):              
        return self.mass
        
    """This function returns the radius of the ball object as a scalar value."""    
    def getRadius(self):            
        return self.radius
        
    """This function returns a 2 element tuple with the x,y position of the ball object.""" 
    def getPosition(self):          
        return self.position[:]
        
    """This function returns a 2 element tuple with the x and y velocities."""
    def getVelocity(self):          
        return self.velocity[:]
        
    """This function returns a 2 element acceleration with the x and y accelerations."""    
    def getAcceleration(self):      # returns a 2-element tuple with the x and y acceleration values.
        return self.acceleration[:]
    
    """This function sets the mass of the ball object."""   
    def setMass(self, m):
        self.mass = m
        
    """def setRadius(self, r): # r is the new radius of the Ball object. Note, this function will need to undraw the circle, create a new circle with the new radius, and draw it back into the window.
        gr.undraw(self)
        self.radius = r
        self.draw(win)"""
    
    """This function sets the x,y position of the ball object.   The px and py variables 
    are the new x,y values.  The x coordinate of p is assigned to the x coordinate in self.pos, 
    and the y coordinate of p is assigned to the y coordinate in self.pos."""   
    def setPosition(self, px, py):  # px and py are the new x,y values
        self.position[0] = px       # assign to the x coordinate in self.pos the x coordinate of p
        self.position[1] = py       # assign to the y coordinate in self.pos the y coordinate of p
        for i in self.vis:
            c = i.getCenter()
            dx = (self.scale*px)-(c.getX())
            dy = (self.win.getHeight()-(self.scale*py)-(c.getY()))
            i.move(dx, dy)
    def setVelocity(self, vx, vy): # vx and vy are the new x and y velocities
        self.velocity[0] = vx
        self.velocity[1] = vy
    def setAcceleration(self, ax, ay): # ax and ay are new x and y accelerations.
        self.acceleration[0] = ax
        self.acceleration[1] = ay
    
    """This function fills the area of the ball with a random color, and sets its outline to a different random color and a width of 3."""  
    def randomcolor(self):
        for i in self.vis:
            i.setFill(gr.color_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            i.setOutline(gr.color_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            i.setWidth(3)
    
    """This function fills the area of the ball with the color red and sets its outline to red with a width of 3."""        
    def red(self):
        for i in self.vis:
            i.setFill("red")
            i.setOutline("red")
            i.setWidth(3)
    
    """This function moves the ball object 1 unit in the left x direction."""       
    def moveLeft(self):
        self.setPosition(self.position[0]-4, self.position[1])
    
    """This function moves the ball object 1 unit in the right x direction."""
    def moveRight(self):
        self.setPosition(self.position[0]+1, self.position[1])
        
    def accelerate(self):
        self.setAcceleration(self.accelerate[0]*2, self.setacceleration[1]*2)
        
    """This function adjust the position, velocity, and vis values of the ball object through 
    dependence on its current acceleration and force values.  It takes one argument (dt), 
    which is the time step that indicates how much time to run the simulation for."""
    def update(self, dt):
        # update the x position using x_new = x_old + x_vel*dt + 0.5*x_acc * dt*dt
        self.position[0] = self.position[0] + self.velocity[0]*dt + 0.5*self.acceleration[0] * dt*dt
        # update the y position using y_new = y_old + y_vel*dt + 0.5*y_acc * dt*dt 
        self.position[1] = self.position[1] + self.velocity[1]*dt + 0.5*self.acceleration[1] * dt*dt
        
        # assign to dx the x velocity times dt times the scale factor (self.scale)
        dx = self.velocity[0]*dt*self.scale
        # assign to dy the negative of the y velocity times dt times the scale factor (self.scale)
        dy = -(self.velocity[1]*dt*self.scale)
        # for each item in self.vis
        for i in self.vis:
            # call the move method of the graphics object with dx and dy as arguments.
            i.move(dx, dy)

        # update the x velocity by adding the acceleration times dt to its old value
        self.velocity[0] = self.velocity[0]+(self.acceleration[0]*dt)
        # update the y velocity by adding the acceleration times dt to its old value
        self.velocity[1] = self.velocity[1]+(self.acceleration[1]*dt)

class Block:

    def __init__(self, win, dx=0, dy=0):
        self.win = win
        self.dx = dx
        self.dy = dy
        self.position = [0,0]
        self.velocity = [0,0]
        self.acceleration = [0,0]
        self.scale = 10
        self.vis = [gr.Rectangle(gr.Point((self.position[0]-self.dx/2)*self.scale, (self.position[1]-self.dy/2)*self.scale), gr.Point((self.position[0]+self.dx/2)*self.scale, (self.position[1]+self.dy/2)*self.scale))]
    
    
    def draw(self):
        for i in self.vis:
            i.draw(self.win)
            
    def undraw(self):
        for i in self.vis:
            i.undraw()
            
    def getPosition(self):          # returns a 2-element tuple with the x, y position.
        return self.position[:]
        
    def setPosition(self, px, py):  # px and py are the new x,y values
        self.position[0] = px       # assign to the x coordinate in self.pos the x coordinate of p
        self.position[1] = py       # assign to the y coordinate in self.pos the y coordinate of p
        for i in self.vis:
            c = i.getCenter()
            dx = (self.scale*px)-(c.getX())
            dy = (self.win.getHeight()-(self.scale*py)-(c.getY()))
            i.move(dx, dy)
            
    def getVelocity(self):          # returns a 2-element tuple with the x and y velocities.
        return self.velocity[:]
        
    def setVelocity(self, vx, vy): # vx and vy are the new x and y velocities
        self.velocity[0] = vx
        self.velocity[1] = vy
        
    def getAcceleration(self):      # returns a 2-element tuple with the x and y acceleration values.
        return self.acceleration[:]
    
    def setAcceleration(self, ax, ay): # ax and ay are new x and y accelerations.
        self.acceleration[0] = ax
        self.acceleration[1] = ay
        
    """def setWidth(self):
        self.width = dx
    
    def setHeight(self):
        self.height = dy"""
        
    def blockcolor(self):
        for i in self.vis:
            i.setFill("grey")
            i.setOutline("black")
            i.setWidth(3)
        
    def update(self, dt):
        # update the x position using x_new = x_old + x_vel*dt + 0.5*x_acc * dt*dt
        self.position[0] = self.position[0] + self.velocity[0]*dt + 0.5*self.acceleration[0] * dt*dt
        # update the y position using y_new = y_old + y_vel*dt + 0.5*y_acc * dt*dt 
        self.position[1] = self.position[1] + self.velocity[1]*dt + 0.5*self.acceleration[1] * dt*dt
        
        # assign to dx the x velocity times dt times the scale factor (self.scale)
        dx = self.velocity[0]*dt*self.scale
        # assign to dy the negative of the y velocity times dt times the scale factor (self.scale)
        dy = self.velocity[1]*dt*self.scale
        # for each item in self.vis
        for i in self.vis:
            # call the move method of the graphics object with dx and dy as arguments.
            i.move(dx, -dy)

        # update the x velocity by adding the acceleration times dt to its old value
        self.velocity[0] = self.velocity[0]+(self.acceleration[0]*dt)
        # update the y velocity by adding the acceleration times dt to its old value
        self.velocity[1] = self.velocity[1]+(self.acceleration[1]*dt)
    

    def collision(self, ball):
        if (abs(ball.position[1]-self.position[1]))<(ball.radius+(self.dy)/2):  #if the ball is colliding with the block
            if (abs(ball.position[0]-self.position[0]))<(ball.radius+(self.dx)/2):
                #print(ball.position)
                #print(self.position)
                return True
        else:
            return False
