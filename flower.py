import turtle as trtl

p = trtl.Turtle()
p.speed(0)
trtl.bgcolor("lightblue")
f = p.forward
r = p.right
l = p.left




p.pensize(25)
p.pencolor("green")
r(90)
f(200)
r(180)
f(275)
p.pencolor('darkgoldenrod2')
p.pensize(200)
f(0)
p.pencolor("burlywood4")
p.pensize(100)
f(0)
r(180)
p.penup()
f(175)
p.pendown()
p.pensize(25)
p.pencolor("green")
p.setheading(270)
p.circle(20,120,20)
p.setheading(90)
p.goto(0,-60)
r(180)
f(225)
r(90)
p.pensize(100)
f(500)
r(180)
f(1000)
r(90)
f(75)
r(90)
f(1000)
r(180)
p.penup()
f(500)
l(90)
f(600)
l(90)
f(300)
p.pendown()
p.pensize(200)
p.pencolor("gold")
f(0)
r(180)
p.penup()
f(500)
p.pensize(100)
p.pendown()
p.pencolor("white")
f(150)
r(180)
f(50)
r(90)
f(50)
l(90)
f(50)

wn = trtl.Screen()
wn.mainloop()
