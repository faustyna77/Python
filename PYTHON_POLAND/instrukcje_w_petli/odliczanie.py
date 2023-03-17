import time

# Napisz swój kod poniżej
num = int(input("Od czego zaczniemy?"))
for i in range(num, 0, -1):
    print(i)
    time.sleep(1)
print("Odliczanie zakończone!")
