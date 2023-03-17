import turtle

t = turtle.Turtle()
# Napisz swój kod poniżej
kolory = ["gold", "red", "green", "cyan", "blue", "khaki"]
for i in range(6):
    t.color(kolory[i])
    t.forward(100)
    t.backward(50)
    t.left(45)
    t.forward(50)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.backward(50)
    t.left(45)
    t.backward(50)
    t.left(60)