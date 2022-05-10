'''

Questão 3 - AV1 - Fabio Pessoa, Rachel Vitória, Rodrigo Brito, Thiago Daniel.

Elaborar um algoritmo que leia uma matriz 12x12 de números inteiros, calcule e escreva o maior e o
menor elemento da área hachurada na figura abaixo, bem como suas respectivas posições.

    A Area hachurada exigida se mostra ocupando a diagonal principal da matriz junto com os
     itens abaixo da mesma.

'''

import random

# Declarando variávies da matriz 12 x 12.
matriz , min , max , tam = [] , 0 , 999 , 12

# Contruindo a matriz:
for i in range( tam ):

    linha = []

    for j in range( tam ):

        num = random.randint( min , max )
        linha.append( num )

    matriz.append( linha )

# Declarando variaveis para a verificação da matriz.
maior , maior_i , maior_j , quant_a = min , [] , [] , 0
menor , menor_i , menor_j , quant_b = max , [] , [] , 0

for i in range( tam ):

    for j in range( tam ):

        if ( i >= j ):

            if ( matriz[i][j] == maior ):

                maior_i.append( i + 1 )
                maior_j.append( j + 1 )
                quant_a += 1

            elif ( matriz[i][j] > maior ):

                maior_i , maior_j = [] , []
                maior = matriz[i][j]
                maior_i.append( i + 1 )
                maior_j.append( j + 1 )
                quant_a = 1

            elif ( matriz[i][j] == menor ):

                menor_i.append( i + 1 )
                menor_j.append( j + 1 )
                quant_b += 1

            elif ( matriz[i][j] < menor ):

                menor_i , menor_j = [] , []
                menor = matriz[i][j]
                menor_i.append( i + 1 )
                menor_j.append( j + 1 )
                quant_b = 1

for i in range( tam ):

    for j in range( tam ):

        if ( i > j ) and ( matriz[i][j] == maior ):
            print ()





