import turtle
import random

t = turtle.Turtle()
count = 0
# Napisz swój kod poniżej
for i in range(3):
    r = random.randint(20, 30)
    t.circle(r)
    x = int(input("Zgadnij promień:"))
    if x == r:
        count = count + 1
t.write(count)