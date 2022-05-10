'''

'''

import random

# Atribuições das váriaveis:
# - <tam> : Dimensão da matriz quadrada;
# - <min> , <max> : Valores mínimo e máximo que podem ser atribuidos à uma célula;
# - <matriz> : lista vazia para a criação da matriz.
# O comentário adicionado nas linhas 14 e 15 permite a modificação das variáveis
# caso deseje atribuir via teclado.

# tam , min = int(input('Tamanho da matriz:')) , int(input('Valor mínimo:'))
# max , matriz = int(input('Valor máximo:')) , []
tam , min , max , matriz = 12 , 0 , 999 , []

# Semente da função random
random.seed(15)

for i in range( tam ):

	# Criação da matriz:
	# - Lista vazia <linha> criada para ser adicionados os valores coluna por
	# coluna na lista;
	# - Variável <num> criada e gerada aleatóriamente e adicionada a lista <linha>.
	linha = []
	for j in range( tam ):

		# Condicional opcional para melhor vizualização da área de atuação do código.
		# (Retirando as áspas triplas das linhas 32 e 35 e adicionando # a linha 37).
		'''if ( j >= i ):
			num = 0
		else:
			num = random.randint( min , max )'''

		num = random.randint( min , max )
		linha.append( num )
	matriz.append( linha )

print( '\nMatriz ' , tam , 'x' , tam , ':\n' )


# Impressão da matriz, format 4 para melhor espaçamento com 3 digitos
for i in range( tam ):

	for j in range( tam ):

		print('{:4}' .format( matriz[i][j] ) , end = '\t')
	print('\n\t')

# Criação das variáveis:
# - <maior> , <menor> : Armazena os valores das celulas de maior e menor valor.
# - <maior_i> , <menor_i> : Armazena em qual linha a(s) maior(es) e menor(es)
# celulas se encontram.
# - <maior_j> , <menor_j> : Armazena em qual coluna a(s) maior(es) e menor(es)
# celulas se encontram.
# - <quant_a> , <quant_b> : Armazena a quantidade de vezes o maior/menor valor se
# repete.
maior , maior_i , maior_j , quant_a = min , [] , [] , 0
menor , menor_i , menor_j , quant_b = max , [] , [] , 0


# "Escaneamento" da matriz.
for i in range(tam):

	for j in range(tam):

		# Condicional para operar somente na area de interesse.
		if ( j <= i ):

			# Condicional para:
			# - Encontrar um valor igual ao armazenado em <maior>;
			# - Armazenar os valores de linha e coluna dessa celula em <maior_i> e
			# <maior_j>;
			# - Adicionar 1 ao contador de vezes que o valor foi encontrado.
			if   ( matriz[i][j] == maior ):

				maior_i.append(i+1)
				maior_j.append(j+1)
				quant_a += 1

			# Condicional para:
			# - Encontrar um valor maior que o <maior> já encontrado;
			# - Armazenar o novo valor na variavel <maior>;
			# - Apagar os valores de linhas e colunas já encontrados;
			# - Zerar o contador de quantas vezes o valor foi encontrado.
			elif ( matriz[i][j] > maior ):

				maior = matriz[i][j]
				maior_i , maior_j = [] , []
				maior_i.append(i+1)
				maior_j.append(j+1)
				quant_a = 0

			# Condicional para:
			# - Encontrar um valor igual ao armazenado em <menor>;
			# - Armazenar os valores de linha e coluna dessa celula em <menor_i> e
			# <menor_j>;
			# - Adicionar 1 ao contador de vezes que o valor foi encontrado.
			elif ( matriz[i][j] == menor ):

				menor_i.append(i+1)
				menor_j.append(j+1)
				quant_b += 1

			# Condicional para:
			# - Encontrar um valor menor que o <menor> já encontrado;
			# - Armazenar o novo valor na variavel <menor>;
			# - Apagar os valores de linhas e colunas já encontrados;
			# - Zerar o contador de quantas vezes o valor foi encontrado.
			elif ( matriz[i][j] < menor ):

				menor = matriz[i][j]
				menor_i , menor_j = [] , []
				menor_i.append(i+1)
				menor_j.append(j+1)
				quant_b = 0

# Condicionais para:
# - Determinar se há uma ou mais célular para imprimir o texto de forma correta.
if ( quant_a == 0 ):
	print( f'\nO maior número na área de interesse é' , maior
		   , f'na posição ({ maior_i[0] } x { maior_j[0] }).')

else:
	print( '\nO maior número na área de interesse é' , maior , ' nas posições:')

	for d in range( quant_a + 1 ):
		print( f'({ maior_i[d] } x { maior_j[d] })', end = '\t')

if ( quant_b == 0 ):
	print( '\nO menor número na área de interesse é' , menor
		   , f'na posição ({ menor_i[0] } x { menor_j[0] }).')

else:
	print( '\nO menor número na área de interesse é' , menor , ' nas posições:')

	for d in range( quant_b + 1 ):
		print( f'({ menor_i[d] } x { menor_j[d] })', end = '\t')
