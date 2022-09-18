from turtle import *




def test():
    for n in range(12):
        côté=30
        penup()
        forward(10)
        fd(100)
        for m in range(12):
            fd(30)
            speed(0)
            penup()
            left(30)
            pendown()
            circle(côté, 180)
        penup()
        backward(100)
        left(30)
        pendown()



test()
end_fill()
exitonclick()


def test2():
    for n in range(12):
        fd(100)
        left(10)

test()
test2()