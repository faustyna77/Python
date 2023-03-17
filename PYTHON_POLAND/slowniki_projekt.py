#zad1 demonstracja 
import time

rooms = {
    'Start': {'rooms': ['1'], 'items':[]},
    '1': {'rooms': ['Start', '2', '3'], 'items':[]},
    '2': {'rooms': ['1'], 'items':['key']},
    '3': {'rooms': ['1', '4'], 'items':[]},
    '4': {'rooms': ['3', '5'], 'items': []},
    '5': {'rooms': ['4', 'Exit'], 'items':[]}
}

room = 'Start'
key = False
while True:
    print('============================')
    print('Jesteś w pokoju', room)
    for near_room in rooms[room]['rooms']:
        print('Możesz iść do pokoju', near_room)
    new_room = input('Który pokój wybierasz? ')
    if new_room not in rooms[room]['rooms']:
        print('Ten pokój nie istnieje!')
        time.sleep(2)
        continue

    if new_room == 'Exit' and not key:
        print('Nie masz klucza, żeby wejść!')
        time.sleep(2)
        continue
    
    if new_room == 'Exit':
        print('Wygrałeś!')
        time.sleep(2)
        break
    
    room = new_room
    if 'key' in rooms[room]['items']:
        key = True
        print('Znalazłeś klucz!')
        rooms[room]['items'].remove('key')
        time.sleep(2)



        #zad2 pokoje

        import time 

rooms = {
    'Start': ['1'],
    '1': ['Start', '2', '3'],
    '2': ['1'],
    '3': ['1', '4'],
    '4': ['3', '5'],
    '5': ['4', 'Exit']
}

#zad3  główna pętla
import time 

rooms = {
    'Start': ['1'],
    '1': ['Start', '2', '3'],
    '2': ['1'],
    '3': ['1', '4'],
    '4': ['3', '5'],
    '5': ['4', 'Exit']
}

room = 'Start'
while True:
    print('============================')
    print('Jesteś w pokoju', room)
    for near_room in rooms[room]:
        print('Możesz iść do pokoju', near_room)
#zad 4 przemieszczanie się
import time

rooms = {
    'Start': ['1'],
    '1': ['Start', '2', '3'],
    '2': ['1'],
    '3': ['1', '4'],
    '4': ['3', '5'],
    '5': ['4', 'Exit']
}

room = 'Start'
while True:
    print('============================')
    print('Jesteś w pokoju', room)
    for near_room in rooms[room]:
        print('You can go to the room', near_room)

    new_room = input('Który pokój wybierzesz? ')
    if new_room not in rooms[room]:
        print('Ten pokój nie istnieje!')
        time.sleep(2)
        continue

    if new_room == 'Exit':
        print('Wygrywasz!')
        time.sleep(2)
        break
#zad5 klucz 
import time

rooms = {
    'Start': {'rooms': ['1'], 'items':[]},
    '1': {'rooms': ['Start', '2', '3'], 'items':[]},
    '2': {'rooms': ['1'], 'items':['key']},
    '3': {'rooms': ['1', '4'], 'items':[]},
    '4': {'rooms': ['3', '5'], 'items': []},
    '5': {'rooms': ['4', 'Exit'], 'items':[]}
}

room = 'Start'
key = False
while True:
    print('============================')
    print('Jesteś w pokoju:', room)
    for near_room in rooms[room]['rooms']:
        print('Możesz iść do pokoju:', near_room)
    new_room = input('Który pokój wybierasz? ')
    if new_room not in rooms[room]['rooms']:
        print('Ten pokój nie istnieje!')
        time.sleep(2)
        continue

    if new_room == 'Exit' and not key:
        print('Nie masz klucza do wejścia!')
        time.sleep(2)
        continue
    
    if new_room == 'Exit':
        print('Wygrywasz!')
        time.sleep(2)
        break
    
    room = new_room
    if 'key' in rooms[room]['items']:
        key = True
        print('Znajdujesz klucz!')
        rooms[room]['items'].remove('key')
        time.sleep(2)


    #powtórzenie wiadomosci
    phoneNumbers = {}
phoneNumbers["John"] = "555-1234"
print(phoneNumbers)



pass_manager = {}

for i in range(0, 3):
    x = input('Nazwa zasobu: ')
    y = input('Hasło: ')
    pass_manager[x] = y

x = input('Nazwa zasobu:')
print(pass_manager[x])


#zadanie domowe 
import time

rooms = {
    'start': {'rooms': ['1'], 'items':[]},
    '1': {'rooms': ['start', '2'], 'items':[]},
    '2': {'rooms': ['1', '3', '4'], 'items':[]},
    '3': {'rooms': ['2'], 'items':[]},
    '4': {'rooms': ['2', '5', '6'], 'items': []},
    '5': {'rooms': ['4'], 'items':['key']},
    '6': {'rooms': ['4', '7'], 'items':[]},
    '7': {'rooms': ['10', '8', '6'], 'items':[]},
    '8': {'rooms': ['7', '9'], 'items':['key']},
    '9': {'rooms': ['8'], 'items':[]},
    '10': {'rooms': ['7', '11'], 'items':[]},
    '11': {'rooms': ['10', '12'], 'items':[]},
    '12': {'rooms': ['Exit', '11'], 'items':[]},
}

room = 'start'
keys = 0
while True:
    print('============================')
    print('Jesteś w pokoju:', room)
    for near_room in rooms[room]['rooms']:
        print('Możesz iść do pokoju:', near_room)
    new_room = input('Który pokój wybierzesz? ')
    if new_room not in rooms[room]['rooms']:
        print('Ten pokój nie istnieje!')
        time.sleep(2)
        continue

    if new_room == 'Exit' and keys != 2:
        print('Nie masz klucza do tych drzwi!')
        time.sleep(2)
        continue
    
    if new_room == '3':
        print('przegrywasz!')
        time.sleep(2)
        break

    if new_room == 'Exit':
        print('Wygrywasz!')
        time.sleep(2)
        break
    
    room = new_room
    if 'key' in rooms[room]['items']:
        keys += 1
        print('Znajdujesz klucz!')
        rooms[room]['items'].remove('key')
        time.sleep(2)