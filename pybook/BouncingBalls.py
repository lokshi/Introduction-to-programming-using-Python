from tkinter import * # Import tkinter
from random import randrange

# Return a random color string in the form #RRGGBB
def getRandomColor():
    color = "#"
    for j in range(0, 6):
        color += toHexChar(randrange(0, 16)) # Add a random digit
    return color

# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if hexValue <= 9 and hexValue >= 0:
        return chr(hexValue + ord('0'))
    else:  # hexValue <= 15 && hexValue >= 10
        return chr(hexValue - 10 + ord('A'))
        
# Define a Ball class
class Ball:
    def __init__(self):
        self.x = 0 # Starting center position
        self.y = 0 
        self.dx = 2 # Move right by default
        self.dy = 2 # Move down by default
        self.radius = 3 # The radius is fixed
        self.color = getRandomColor() # Get random color

class BouncingBalls:
    def __init__(self):
        self.ballList = [] # Create a list for balls
        
        window = Tk() # Create a window
        window.title("Bouncing Balls") # Set a title
        
        self.width = 350 # Width of the self.canvas
        self.height = 150 # Width of the self.canvas
        self.canvas = Canvas(window, bg = "white", 
            width = self.width, height = self.height)
        self.canvas.pack()
        
        frame = Frame(window)
        frame.pack()
        btStop = Button(frame, text = "Stop", command = self.stop)
        btStop.pack(side = LEFT)
        btResume = Button(frame, text = "Resume",
            command = self.resume)
        btResume.pack(side = LEFT)
        btAdd = Button(frame, text = "+", command = self.add)
        btAdd.pack(side = LEFT)
        btRemove = Button(frame, text = "-", command = self.remove)
        btRemove.pack(side = LEFT)
        
        self.sleepTime = 100 # Set a sleep time 
        self.isStopped = False
        self.animate()
        
        window.mainloop() # Create an event loop
           
    def stop(self): # Stop animation
        self.isStopped = True
    
    def resume(self): # Resume animation
        self.isStopped = False   
        self.animate()
    
    def add(self): # Add a new ball
        self.ballList.append(Ball())
    
    def remove(self): # Remove the last ball 
        self.ballList.pop()
                                
    def animate(self): # Move the message
        while not self.isStopped:
            self.canvas.after(self.sleepTime) # Sleep 
            self.canvas.update() # Update self.canvas
            self.canvas.delete("ball") 
            
            for ball in self.ballList:
                self.redisplayBall(ball)
    
    def redisplayBall(self, ball):
        if ball.x >= self.width:
            ball.dx = -2
        elif ball.x < 0:
            ball.dx = 2
            
        if ball.y >= self.height:
            ball.dy = -2
        elif ball.y < 0:
            ball.dy = 2
    
        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius, 
            ball.y - ball.radius, ball.x + ball.radius, 
            ball.y + ball.radius, fill = ball.color, tags = "ball")
                                             
BouncingBalls() # Create GUI