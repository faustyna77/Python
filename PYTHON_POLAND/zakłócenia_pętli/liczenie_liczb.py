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