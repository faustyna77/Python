import turtle

t = turtle.Turtle()
num = int(input("Liczba iteracji:"))
distance = int(input("Dystans:"))
angle = int(input("Kąt:"))
# Wpisz swój kod poniżej
for i in range(num):
    t.forward(distance)
    t.left(angle)