import turtle
# turtle.fillcolor("Black")
# turtle.begin_fill()
# turtle.pencolor("Red")
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.end_fill()
# turtle.done()

pop = turtle.Turtle()
pop.speed(50)
def saule(x,y):
    pop.getscreen().bgcolor('orange')
    pop.pencolor('red')
    pop.penup()
    pop.goto(x,y)
    pop.pendown()
    for i in range(100):
        pop.forward(100)
        pop.right(180)
        pop.forward(100)
        pop.left(40)
        
  
turtle.onscreenclick(saule,1)
turtle.listen()

turtle.done()