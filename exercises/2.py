'''
Elaborar um algoritmo que leia 12 números binários, isto é, somente serão permitidos números “0s” ou “1s” (deve-se
    fazer a proteção de dados). Calcule e imprima:

    • A quantidade de números “1s” e números “0s”. Deve-se também comparar os resultados para saber se existem
mais “1s” ou “0s” ou se as quantidades são iguais (deve-se imprimir uma mensagem ao usuário);
    • O percentual de números “0s” e “1s” digitados.
'''

z , u = 0 , 0

print('Bem vindo ao contador binário.')
for c in range (1,13):
    while True:
        x=int(input('Entre com zeros ou uns:'))
        if x==0 or x==1:
            break
        else:
            print('Inválido')
    if x==1:
        u+=1
    else:
        z+=1
pz=(z/12)*100
pu=(u/12)*100
print('Foram inseridos',z,'zeros e',u,'uns.')
print('A porcentagem de zeros é de {:.1f}% e de uns é de {:.1f}%.' .format(pz,pu))
