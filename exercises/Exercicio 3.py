print('Contador estatistico números entre 1 e 99.')

c, s, c1_10, a, mid5 = 0, 0, 0, 0, 100

while True:
    print('Digite números entre 1 e 99.\n Digite 0 para sair.')
    n=int(input())
    if n>=0 and n<=99:
        break
    else:
        print('Número não computado.')

while n!=0:
    s+=n
    c+=1
    if n>=1 and n<=10:
        c1_10+=1
    while True:
        print('Digite números entre 1 e 99.\n Digite 0 para sair.')
        n = int(input())
        if n >= 0 and n <= 99:
            break
        else:
            print('Número não computado.')
    if n%5==0 and n%2==1 and n<mid5:
        a+=1
        mid5=n

if c==0:
    print('Nenhum número computado.')
else:
    m=s/c
    print('A média de todos os números inseridos é: {:.2f}' .format(m))
    if c1_10==0:
        print('Nenhum valor entre 1 e 10 inserido.')
    else:
        p1_10=(c1_10/c)*100
        print('A porcentagem de números entre 1 e 10 é de {:.2f}%'.format(p1_10))
    if a==0:
        print('Nenhum número impar divisivel por 5 foi inserido.')
    else:
        print('O menor impar divisível por 5 inserido foi:',mid5)