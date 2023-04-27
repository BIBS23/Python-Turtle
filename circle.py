import turtle
t = turtle.Turtle()
def drawCircle(x,y,rad,color):
    t.up()
    t.goto(x,y)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
drawCircle(0,0,30,'red')
drawCircle(60,0,30,'green')
drawCircle(12,0,30,'blue')
turtle.done()
