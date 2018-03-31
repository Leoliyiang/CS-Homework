import turtle           # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def orange():
    tess.forward(70)
    tess.fillcolor("orange")
    wn.ontimer(red,2000)


def red():
    tess.forward(70)
    tess.fillcolor("red")
    wn.ontimer(green,2000)


def green():
    tess.back(140)
    tess.fillcolor("green")
    wn.ontimer(orange,2000)

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()
    tess.penup()
    # Position tess onto the place where the green light should be
    tess.forward(40)
    tess.left(90)
    tess.forward(50)
    # Turn tess into a big green circle
    tess.shape("circle")
    tess.shapesize(3)
    tess.fillcolor("green")
    wn.ontimer(orange,2000)
# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine




# Bind the event handler to the space key.

draw_housing()
wn.listen()                      # Listen for events
wn.mainloop()