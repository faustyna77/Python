import random

count = 0
while True:
    x = random.randint(1, 10)
    answer = int(input("Zgadnij liczbę:"))
    # Wprowadź kod poniżej
    if answer == x:
        print("Dobrze! +1 punkt!")
        count = count + 1
    else:
        print ("Więcej szczęścia następnym razem!")
    game = input("Czy chcesz przestać grać?")
    if game == "tak":
        break
print("Wynik:", count)
