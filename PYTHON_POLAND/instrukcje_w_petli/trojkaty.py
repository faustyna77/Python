import turtle

t = turtle.Turtle()
# Napisz swój kod poniżej
for i in range(3):
    distance = int(input("Wprowadź rozmiar:"))
    if distance > 0 and distance <= 100:
        t.forward(distance)
        t.left(120)
        t.forward(distance)
        t.left(120)
        t.forward(distance)
        t.left(120)
    else:
        t.write("Error")