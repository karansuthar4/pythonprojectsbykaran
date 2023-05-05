import turtle
t1=turtle.Turtle()
direction=input("want to go (f) forward or(b) backward=").lower()
point=int(input("enter how many points="))

if direction=="f":
    t1.fd(point)
elif direction=="b":
    t1.backward(point)

turtle.done()
