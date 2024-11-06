import keyboard
import random
import time
a = input("Combien de faces veux-tu ?")
b = input("Combien de dés veux-tu ?")
c = int(a)
d = int(b)
for i in range(0, d):
    e = random.randint(1, c)
    print(e)
    time.sleep(1)
while True:
    time.sleep(0.001)
    if keyboard.read_key() == "q":
        break