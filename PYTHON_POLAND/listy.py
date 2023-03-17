
#zad indeksy
lista = ["zerowy", "pierwszy", "drugi", "trzeci"]
print(lista[-1])

for i in range(4):
    print(i, lista[i])

#ujemne

lista = [-8, 12, 9, -45, -1]
# Napisz swój kod poniżej
for i in range(5):
    if lista[i] < 0:
        print(lista[i])


#zad2
pr_lista = []
for i in range(3):
    przyjaciel = input("Dodaj imię przyjaciela:")
    pr_lista.append(przyjaciel)
print(pr_lista)

#zad3 lista zakupów 
produkty = []
x = int(input("Ile produktów znajdzie się na liście:"))
# Napisz swój kod poniżej
for i in range(x):
    prod = input("Dodaj produkt:")
    produkty.append(prod)
print(produkty)
    
#zad4 czat bot
import random

filmy = ["Co w duszy gra", "Kopciuszek", "Mulan", "Megamocny", "Zaplątani", "Vaiana", "Zootopia", "Auta"]

while True:
    command = input("Podaj komendę:")
    # Napisz swój kod poniżej
    if command == "wyświetl":
        print(filmy)
    if command == "dodaj":
        x = input("Jaki film chcesz dodać:")
        filmy.append(x)
    if command == "usuń":
        x = input("Jaki film już obejrzałeś:")
        filmy.remove(x)
    if command == "wyjdź":
        break
        
#zad5 kolorowy płatek śniegu
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


#zad6 losowa lista 
import random

lista = []
# Napisz swój kod poniżej
for i in range(5):
    x = random.randint(10, 100)
    lista.append(x)
print(lista)



