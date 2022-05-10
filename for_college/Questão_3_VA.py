'''

Questão 3 - AV1 - Fabio Pessoa, Rachel Vitória, Rodrigo Brito, Thiago Daniel.

Elaborar um algoritmo que leia uma matriz 12x12 de números inteiros, calcule e escreva o maior e o
menor elemento da área hachurada na figura abaixo, bem como suas respectivas posições.

    A Area hachurada exigida se mostra ocupando a diagonal principal da matriz junto com os
     itens abaixo da mesma.

    valor da linha deve ser maior ou igual ao da coluna
'''

import random
#random.seed(15)

# Declarando variáveis:
matriz , tam , min, max = [] , 12 , 0 , 999

# Gerando a matriz
for i in range ( tam ):

    linha = []

    for j in range ( tam ):

        num = random.randint( min , max )
        linha.append( num )

    matriz.append( linha )

# Declarando variáveis:
maior , maior_i , maior_j , quant_a = min , [] , [] , 0
menor , menor_i , menor_j , quant_b = max , [] , [] , 0

# Coleta de dados:
for i in range ( tam ):

    for j in range ( tam ):

        if ( i >= j ):

            if ( matriz[i][j] == maior ):

                maior_i.append( i + 1 )
                maior_j.append( j + 1 )
                quant_a += 1

            elif ( matriz[i][j] > maior ):

                maior = matriz[i][j]
                maior_i , maior_j = [] , []
                maior_i.append(i + 1)
                maior_j.append(j + 1)
                quant_a = 1

            elif (matriz[i][j] == menor):
                menor_i.append(i + 1)
                menor_j.append(j + 1)
                quant_b += 1

            elif (matriz[i][j] < menor):

                menor = matriz[i][j]
                menor_i, menor_j = [], []
                menor_i.append(i + 1)
                menor_j.append(j + 1)
                quant_b = 1

# Imprimindo a matriz:
for i in range ( tam ):

    for j in range ( tam ):

        if ( matriz[i][j] == maior ) and ( i >= j ):

            print( f'>{matriz[i][j]:^5}<' , end = '\t' )

        elif (matriz[i][j] == menor) and (i >= j):

            print( f'<{matriz[i][j]:^5}>' , end = '\t' )

        else:

            print(f'{matriz[i][j]:^5}', end='\t')

    print('\n')

if ( quant_a == 1 ):

    print( f'\nO maior valor encontrado foi {maior}, na linha {maior_i[0]} com a coluna {maior_j[0]}')

else:

    print(f'\nO maior valor encontrado foi {maior}, nas posições:')

    for c in range( quant_a ):

        print( f'\n({maior_i[c]} x {maior_j[c]})')
if ( quant_b == 1 ):

    print( f'\nO menor valor encontrado foi {menor}, na linha {menor_i[0]} com a coluna {menor_j[0]}')

else:

    print(f'\nO menor valor encontrado foi {menor}, nas posições:')

    for c in range( quant_b ):

        print( f'\n({menor_i[c]} x {menor_j[c]})')

