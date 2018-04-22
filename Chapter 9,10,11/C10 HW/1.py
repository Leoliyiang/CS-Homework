import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle
tess.color("black")

size=3

def pensize_in():
    global size
    size=size+1
    tess.pensize(size)

def pensize_de():
    global size
    size=size-1
    tess.pensize(size)

def tesscolor_y():
    tess.color("yellow")

def tesscolor_g():
    tess.color("green")

def tesscolor_b():
    tess.color("blue")
# The next four functions are our "event handlers".
def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()                        # Close down the turtle window

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(tesscolor_y, "y")
wn.onkey(tesscolor_b, "b")
wn.onkey(tesscolor_g, "g")
wn.onkey(pensize_in(), "+")
wn.onkey(pensize_de(), "-")
# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()