import turtle
import random

t = turtle.Turtle()
t.up()
t.goto(-100,100)
t.down()
t.speed(0)

# pole wyścigowe
for i in range(15):
    t.write(i)
    t.right(90)
    t.forward(200)
    t.left(180)  
    t.forward(200)
    t.right(90)
    t.forward(20)

# tworzenie żółwi
first = turtle.Turtle()
first.shape("turtle")
first.color("red")
first.up()
first.goto(-120,70)
first.down()

second = turtle.Turtle()
second.shape("turtle")
second.color("blue")
second.up()
second.goto(-120,40)
second.down()

third = turtle.Turtle()
third.shape("turtle")
third.color("yellow")
third.up()
third.goto(-120,10)
third.down()

for i in range(3):
    fan = turtle.Turtle()
    fan.shape("turtle")
    fan.color('#800080')
    fan.up()
    fan.goto(-90+25*i,-120)
    fan.down()
    fan.left(90)

x_first = 0
x_second = 0
x_third = 0

win = input("Który żółw wygra?:")
text = turtle.Turtle()
text.up()
text.goto(-120,120)
text.write("Myślisz, że zwycięzcą będzie " + win)

while True:
    if x_first > 305 or x_second > 305 or x_third > 305:
        break
    first_step = random.randint(1,5)
    x_first = x_first + first_step
    first.forward(first_step)
    
    second_step = random.randint(1,5)
    x_second = x_second + second_step
    second.forward(second_step)
    
    third_step = random.randint(1,5)
    x_third = x_third + third_step
    third.forward(third_step)
