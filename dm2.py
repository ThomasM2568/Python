from turtle import *
speed(0)
colormode(255)
penup()
left(90)
fd(70)
right(90)
pendown()

def polygone():
    for k in range(5):
        forward(100)
        left(72)


def rosace2():
    for w in range(72):
        polygone()
        right(10)
        pencolor(1*w, 2*w, 3*w)

def test():

    for z in range(9):
        rosace2()
        fd(100)
        right(40)


test()
exitonclick()