#   a115_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
legs = 8
leg_length = 70
turtle_direction = 360 / legs
spider.pensize(5)
loop_variable = 0
while (loop_variable < legs):
  spider.goto(0,20)
  spider.setheading(turtle_direction*loop_variable)
  spider.forward(leg_length)
  loop_variable+=1
spider.hideturtle()
wsn = trtl.Screen()
wn.mainloop()