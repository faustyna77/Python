count = 0
for i in range(5):
    x = int(input("Wpisz numer:"))
    if x < 0:
        count = count + 1
print("Ilość liczb ujemnych:", count)
