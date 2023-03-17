import turtle

t = turtle.Turtle()
t.color(237, 76, 103)
for i in range(8): # Pętla zostanie wykonana 8 razy
    # Ten kod zostanie wykonany w pętli, ponieważ są tutaj wcięcia
    t.circle(50)
    t.left(45)
# Ten kod zostanie wykonany po wykonaniu pętli, ponieważ wcięty blok się zakończył
t.write ("Koniec pętli!")