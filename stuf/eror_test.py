import turtle
turtle.showturtle()
def house(g,b):
    turtle.shape(g)
    turtle.pencolor(b)
    x = 50
    for i in range(10):
        for h in range(4):
            turtle.forward(x)
            turtle.right(90)
            x += 10
house("turtle","pink")
