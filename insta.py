from turtle  import*
import colorsys
t=Turtle()
speed(0)
Screen().bgcolor("black")
pensize(2)
n=100
h=0
for i in range(36):
    for i in range(4):
        c=colorsys.hsv_to_rgb(h,1,0.6)
        h+=1/n
        color(c)
        circle(40+i*5,90)
        fd(100)
        lt(90)
    rt(10)
done()

# import turtle
# t=turtle.Turtle()
# i=1
# t.circle(40+i*5,90)
# turtle.done()