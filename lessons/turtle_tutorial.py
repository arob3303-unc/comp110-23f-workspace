from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.penup()
leo.goto(-350, -250)
leo.pendown()
leo.pencolor(19, 203, 204)
leo.fillcolor(0, 0, 0)
leo.speed(10)
leo.hideturtle()


leo.begin_fill()

side_length: int = 700

i1: int = 0
while (i1 < 3):
    leo.forward(side_length)
    leo.left(120)
    
    i1 += 1

leo.end_fill()

bob: Turtle = Turtle()

bob.penup()
bob.goto(-350, -250)
bob.pendown()
bob.pencolor("Purple")
bob.speed(50)
bob.ht()

i2: int = 0
while (i2 < 555):
    bob.forward(side_length)
    bob.left(120)
    side_length *= 0.90
    i2 += 1



done()