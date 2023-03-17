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
