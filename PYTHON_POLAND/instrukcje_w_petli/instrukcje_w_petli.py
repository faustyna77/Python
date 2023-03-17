import random

count = 0
for i in range(10):
    x = random.randint(1, 6)
    if x >= 5:
        print(x, "Uciekłeś przed potworem!")
        count = count + 1
    else:
        print(x, "Nie tym razem. Potwór cię dogonił...")
print("Uciekłeś przed potworem:", count, "razy.")