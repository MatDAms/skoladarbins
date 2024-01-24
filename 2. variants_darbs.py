# 1 uzdevums
import turtle
import random
# b = random.randint(50,100) # ieliku random lai mainitu riņķa lielumu
# def aplis():
#     turtle.pencolor("black") # ielieku krasu kad bus zimejumamm
# for x in range(2):
#     b = random.randint(50,100)
#     turtle.circle(b) #izveidoju apli kas zimes 2 reizes citos lielumos
#     turtle.penup()
#     turtle.goto(0,-20) # novietot cita kordinata 
#     turtle.pendown()
#     b += 50
# turtle.done()

# 2 uzdevums

krasa = ['red', 'blue', 'green', 'black','pink']
y = random.choice(krasa)
i = random.randint(0,100)
u = random.randint(100,200)

def izmiaņa():
    turtle.circle(100)
    turtle.getscreen().bgcolor(y)


turtle.onscreenclick(izmiaņa,1)
turtle.listen()
turtle.done()