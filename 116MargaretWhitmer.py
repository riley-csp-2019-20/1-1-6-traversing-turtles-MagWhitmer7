#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#  set starting place and direction
startx = 0
starty = 0
direction=90

# move turtles so they don't overlap
for t in my_turtles:
    new_color=turtle_colors.pop()
    t.pencolor(new_color)
    t.fillcolor(new_color)
    t.begin_fill()
    t.setheading
    t.penup()
    t.end_fill()
    t.goto(startx, starty)
    t.right(45)     
    t.forward(50)
    t.pendown()
    t.end_fill()

#	set new start x and start y
    startx = t.xcor()
    starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()