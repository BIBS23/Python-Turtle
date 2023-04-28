import turtle

t = turtle.Turtle()
t.speed(1)
t.fillcolor('yellow')
t.pensize(5)
t.turtlesize(10.0)
turtle.bgcolor('red')
t.goto(180,0)
t.begin_fill()
t.left(90)
t.circle(200,180)
t.left(90)
t.forward(400)
t.end_fill()
turtle.done()

