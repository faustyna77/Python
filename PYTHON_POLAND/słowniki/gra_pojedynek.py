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