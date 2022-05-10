print("Contador Zeros e Uns")
u=0
z=0
c=12
while(c!=0):
    c-=1
    x=int(input("Entre com um ou zero:"))
    if x==1:
        u+=1
    elif x==0:
        z+=1
    else:
        print("Só será aceito 1 ou 0.")
        c+=1
print("A porcentagem de uns é {:.2f} e a de zeros é {:.2f}." .format(u*100/12, z*100/12))