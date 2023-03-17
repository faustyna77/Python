#zad1 Słownik
phoneNumbers = {}
phoneNumbers["Bob"] = "555-6789"
phoneNumbers["Rock"] = "444-4321" 
phoneNumbers["Steven"] = "867-5309"
print(phoneNumbers)
phoneNumbers = {"John": 2222,"Bob":"000000"}
print(phoneNumbers)
#zad2 menadżer haseł
#nie używaj tego programu do przechowywania prawdziwych haseł
pass_manager = {}

for i in range(0, 3):
    x = input('Nazwa zasobu: ')
    y = input('Hasło: ')
    pass_manager[x] = y

x = input('podaj nazwe zasobu do, którego chcesz uzyskać hasło:')
print(pass_manager[x])

#zad3 metoda słownika
phoneNumbers={"lisa":"555555","marek":"44444","ewa":"99999"}
del phoneNumbers["lisa"]
phonenumbers2={}
phonenumbers2.values()
print(phoneNumbers.values())
print(phonenumbers2)
#zad4 książka telefoniczna
phoneNumbers = {}
phoneNumbers["John"] = "555-1234"
phoneNumbers["Max"] = "555-6789"
phoneNumbers["Steve"] = "444-4321" 
phoneNumbers["Kenny"] = "867-5309"
print(phoneNumbers)

letter = input('Imiona zaczynające się na jaką literę chcesz zobaczyć?') 
for key in phoneNumbers.keys():
    if key[0] == letter:
        print(key, ':', phoneNumbers[key])
#zad 5 gra pojedynek
import time
player1 = {'Name' : "Gracz1", 'Health' : 100, 'Attack' : 10}
player2 = {'Name' : "Gracz2", 'Health' : 100, 'Attack' : 10}

while player1['Health'] > 0 and player2['Health'] > 0:
    player2['Health'] -= player1['Attack']
    print(player1['Name'], ' atakuje ', player2['Name'])
    time.sleep(1)
    player1['Health'] -= player2['Attack']
    print(player2['Name'], 'atakuje', player1['Name'])
    time.sleep(1)
    print('Gracz1 :', player1['Health'], 'Gracz2 :', player2['Health'])

#zad 6 -zadanie domowelista kolegów
phoneNumbers = {}
phoneNumbers["John"] = "555-1234"
phoneNumbers["Max"] = "555-6789"
phoneNumbers["Steve"] = "444-4321" 
phoneNumbers["Kenny"] = "867-5309"
print(phoneNumbers)

letter = input('hobby którego kolegi/koleżanki chcesz poznać?') 


for key in phoneNumbers.keys():
    if key == letter:
        print(key, ':', phoneNumbers[key])
#zad7
str1 = 'Pythonnnn'
my_dict = {i: str1.count(i) for i in str1}
print(my_dict)