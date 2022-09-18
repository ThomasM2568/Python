from turtle import *


def test():
    for n in range(12):
        fd(100)
        for m in range(12):
            forward(25)
            backward(25)
            left(30)
        backward(100)
        left(30)
        


pencolor("blue")
fillcolor("pink")
begin_fill()
test()
end_fill()
exitonclick