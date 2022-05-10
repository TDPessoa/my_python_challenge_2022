import random
import time
print("Contador Zeros e Uns")
u=0
z=0
o=0
c=100
while(c!=0):
    c-=1
    x=random.randint(0,9)
    if x==1:
        u+=1
    elif x==0:
        z+=1
    else:
        o+=1
print("A porcentagem de uns é {:.2f}%, a de zeros é {:.2f}% e de outros é de {:.2f}%." .format(u, z, o))