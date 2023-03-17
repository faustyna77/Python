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