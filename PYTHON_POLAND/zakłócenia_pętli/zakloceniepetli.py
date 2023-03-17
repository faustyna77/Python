while True:
    password = input("Podaj hasło:")
    if password == "admin":
        print("Hasło jest poprawne! Dostęp zatwierdzony!")
        break
    else:
        print("Hasło jest błędne!")