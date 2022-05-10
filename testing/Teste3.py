import random

tam = 12

random.seed(2)

matriz = []

for i in range( tam ):
	linha = []
	for j in range( tam ):
		num = random.randint(0,9)
		linha.append(num)
	matriz.append(linha)

print('\nMatriz ',tam,'x',tam,':\n')

for i in range(tam):
	for j in range (tam):
		print(f'{matriz[i][j]}', end = '\t')
	print('\n')

maior , maior_i , maior_j , quant_a = 0 , [] , [] , 0
menor , menor_i , menor_j , quant_b = 0 , [] , [] , 0

for i in range(tam):

	for j in range(tam):

		if ( j < i ):

			if   ( matriz[i][j] == maior ):

				maior_i.append(i)
				maior_j.append(j)
				quant_a += 1

			elif ( matriz[i][j] > maior ):

				maior = matriz[i][j]
				maior_i , maior_j = [] , []
				maior_i.append(i)
				maior_j.append(j)
				quant_a = 0

			elif ( matriz[i][j] == menor ):

				menor_i.append(i)
				menor_j.append(j)
				quant_b += 1

			elif ( matriz[i][j] < menor ):

				menor = matriz[i][j]
				menor_i , menor_j = [] , []
				menor_i.append(i)
				menor_j.append(j)
				quant_b = 0

if ( quant_a == 0 ):
	print( '\nO maior número abaixo da diagonal principal é' , maior , 'na linha' , maior_i[0] + 1 , 'e coluna' , maior_j[0] + 1 , '.')

else:
	print( '\nO maior número abaixo da diagonal principal é' , maior , ' nas posições:')

	for c in range( quant_a + 1 ):
		print( f'({ maior_i[c]} x {maior_j[c]})', end = '\t')

if ( quant_b == 0 ):
	print( '\nO menor número abaixo da diagonal principal é' , menor , 'na linha' , menor_i[0] + 1 , 'e coluna' , menor_j[0] + 1 , '.')

else:
	print( '\nO menor número abaixo da diagonal principal é' , menor , ' nas posições:')

	for c in range( quant_b + 1 ):
		print( f'({ menor_i[c]} x {menor_j[c]})', end = '\t')