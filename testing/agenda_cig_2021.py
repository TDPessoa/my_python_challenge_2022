'''
Programa para calcular "randomicamente" minha agenda para os dias que ficarei sem cigarros
'''

import random

random.seed(920008966)

for c in range (1, 17):
    if c <= 3:
        x = random.randint(1, 14)
        print(f"{c}|{x}")
    elif c > 3 and c <= 7:
        if c == 4:
            print("--"*40)
        x , y = random.randint(1, 14) , random.randint(1, 14)
        print(f"{c}|{x} + {y}")
    elif c > 7 and c <= 12:
        if c == 8:
            print("--"*40)
        x , y, z = random.randint(1, 14) , random.randint(1, 14), random.randint(1, 14)
        print(f"{c}|{x} + {y} + {z}")
    else:
        if c == 13:
            print("--"*40)
        x, y, z, m = random.randint(1, 14), random.randint(1, 14), random.randint(1, 14), random.randint(1, 14)
        print(f"{c}|{x} + {y} + {z} + {m}")