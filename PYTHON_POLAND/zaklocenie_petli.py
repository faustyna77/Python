#zad1 	Instrukcja warunkowa w pętli while
while True:
    x = int(input("Podaj liczbę:"))
    if x > 0:
        print("Liczba dodatnia")
    elif x < 0:
        print("Liczba ujemna")
    else:
        print("To jest zero.")
        
        
        
#zad2 liczenie liczb 
count_n = 0
count_p = 0
while True:
    x = int(input("Wpisz liczbę:"))
    if x > 0:
        count_p = count_p + 1
    elif x < 0:
        count_n = count_n + 1
    else:
        print("To jest zero")
    print("Liczby dodatnie:", count_p, ", Liczby ujemne:", count_n)
#zad3 zakłócenie działania petli
while True:
    password = input("Podaj hasło:")
    if password == "admin":
        print("Hasło jest poprawne! Dostęp zatwierdzony!")
        break
    else:
        print("Hasło jest błędne!")
#zad3  rekrutacja 
count = 0
while True:
    age = int(input("Podaj swój wiek:"))
    pr = input("Lubisz programować?")
    if age >= 12 and age <= 17 and pr == "tak":
        print("Zespół przyjął!")
        count = count + 1
    else:
        print("Niestety nie spełniasz naszych wymagań")
    if count == 5:
        break
print("Zespół przyjął:", count, "osób")

#zad4 zgadnij numer
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
