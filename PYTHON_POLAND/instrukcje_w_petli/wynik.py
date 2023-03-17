import random

count = 0
# Napisz swój kod poniżej
for i in range(5):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    print(x, "+", y)
    answer = int(input("Twoja odpowiedź:"))
    if answer == x + y:
        print("Odpowiedź jest prawidłowa! +1 punkt!")
        count = count + 1
    else:
        print ("Błąd! Odpowiedź:", x+y)
print ("Twój wynik:", count)