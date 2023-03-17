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