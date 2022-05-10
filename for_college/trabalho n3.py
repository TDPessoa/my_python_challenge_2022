#Elaborar um algoritmo que leia uma matriz 12x12 de números inteiros, calcule e escreva o maior e o menor elemento da área hachurada na figura abaixo, bem como suas respectivas posições.
from random import randint, seed

tam = 12
matriz = []
seed(2)
for i in range(tam):
    linha = []
    for j in range(tam):
         num = randint(-5, 12)
         linha.append(num)
    matriz.append(linha)
print("Matriz 12x12\n")
for i in range(tam):
    for j in range(tam):
        print(f"{matriz[i][j]:^5}", end="\t")
    print("\n")

maior = 0
menor = 0
for i in range(tam):
    for j in range (tam):
        if(i>=j):
            if (matriz[i][j] > maior):
                maior = matriz[i][j]
            if(matriz[i][j] < menor):
                menor = matriz[i][j]

print(f"\nO maior elemento da área hachurada é: {maior} ")
print(f"\nO menor elemento da área hachurada é: {menor}")
