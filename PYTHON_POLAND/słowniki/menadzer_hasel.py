pass_manager = {}

for i in range(0, 3):
    x = input('Nazwa zasobu: ')
    y = input('Hasło: ')
    pass_manager[x] = y

x = input('podaj nazwe zasobu do, którego chcesz uzyskać hasło:')
print(pass_manager[x])