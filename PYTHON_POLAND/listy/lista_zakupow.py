produkty = []
x = int(input("Ile produktów znajdzie się na liście:"))
# Napisz swój kod poniżej
for i in range(x):
    prod = input("Dodaj produkt:")
    produkty.append(prod)
print(produkty)