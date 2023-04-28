import turtle

t = turtle.Turtle()

t.fillcolor('blue')
t.begin_fill()
t.goto(30,0)
for i in range(6):
    t.right(60)
    t.forward(100)
t.end_fill()
t.up()
t.goto(10,100)
t.down()
t.left(20)

for i in range(6):
    t.right(60)
    t.forward(200)

