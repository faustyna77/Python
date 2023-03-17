count = 0
# Napisz swój kod poniżej
for i in range(5):
    age = int(input("Podaj swój wiek:"))
    if age >= 10 and age <= 12:
        print("Zostałeś przyjęty do drużyny!")
        count = count + 1
    else:
        print("Niestety nie spełniasz naszych wymagań.")
print("Rekrutacja zakończona! Jest", count, " osób w drużynie.")
