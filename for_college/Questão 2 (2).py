import random

matriz, tam = [], 10

# Gerando a matriz base

for i in range(tam):

    linha = []

    for j in range(tam):
        linha.append(random.randint(0, 999))
    matriz.append(linha)

# Imprimindo a matriz

for i in range(tam):

    for j in range(tam):
        print(f'{matriz[ i ][ j ]:^4}', end = '\t' )

    print('\n')

    # Separação para identificação

print('-' * 200)

# Troca 1 ( Linha 2 para Linha 8 )

for i in range(tam):
    c = matriz[1][i]
    matriz[1][i] = matriz[7][i]
    matriz[7][i] = c

# Troca 2 ( Coluna 4 para Coluna 10 )

for i in range(tam):
    c = matriz[i][3]
    matriz[i][3] = matriz[i][9]
    matriz[i][9] = c

# Troca 3 (Diagonal Pricipal para Diagonal Secundária )

for i in range(tam):

    for j in range(tam):

        if (i + j == 9):
            c = matriz[i][i]
            matriz[i][i] = matriz[i][j]
            matriz[i][j] = c

# Troca 4 ( Linha 5 para Coluna 10 )

for i in range(tam):
    c = matriz[4][i]
    matriz[4][i] = matriz[i][9]
    matriz[i][9] = c

# Imprimindo a matriz "trabalhada"

for i in range(tam):

    for j in range(tam):
        print(f'{matriz[i][j]:^4}', end='\t')

    print('\n')
