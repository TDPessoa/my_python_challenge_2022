import random
tam = int(input('Número de linhas e colunas da matriz: '))
#random.seed(2)
matriz = []
for i in range(tam):
    linha = []
    for j in range(tam):
        while True:
            num = random.randint(-10,10)
            if (num >= 0) and (num <= 5):
                break
    linha.append(num)
    matriz.append(linha)

print('\nMatriz A\n')
for i in range(tam):
    for j in range (tam):
        print(f'{matriz[i][j]}', end = '\t')
    print('\n')

print('\nMatriz A\n')
for i in range(tam):
    for j in range (tam):
        print(f'{matriz[i][j]}', end = '\t')
    print('\n')

prodc2 , somal4, somadp, somads, somatodos= 1, 0, 0, 0, 0

for i in range(tam):
    for j in range(tam):
        #Soma todos os números da matriz
        somatodos += matriz[i][j]
        #acessar a linha 4
        if (i == 3):
            somal4 += matriz[i][j]
        #Acessar a coluna 2
        if (j == 1):
            prodc2 *= matriz[i][j]
        #Acessar diagonal principal
        if (i == j):
            somadp += matriz[i][j]
        #Acessar diagonal secundária
        if (i+j == tam-1):
            somads += matriz[i][j]

print(f'Soma dos números da L4: {somal4}')
print(f'Produto doa numeros da C2: {prodc2}')
print(f'Soma dos números da DP: {somadp}')
print(f'Soma dos números da DS: {somads}')
print(f'Soma todos os números da matriz: {somatodos}')
