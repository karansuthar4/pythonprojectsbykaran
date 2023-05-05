from turtle import*
import colorsys
bgcolor("black")
speed(6)
tracer(130)
pencolor("blue")
hue=0.7
hideturtle()
pensize(2)

def func():
    global hue
    for i in range(4):
        global hue
        for i in range(4):
            c=colorsys.hsv_to_rgb(hue,1,0.5)
            hue=+0.000001
            fillcolor(c)
            begin_fill()
            fd(100)
            rt(18)
            fd(100)
            lt(22)
            end_fill()
for j in range(400):
    func()
    goto(8,8)
    rt(188)

exitonclick()
