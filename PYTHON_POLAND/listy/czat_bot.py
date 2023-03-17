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
        