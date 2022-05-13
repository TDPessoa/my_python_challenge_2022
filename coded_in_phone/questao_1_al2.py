'''
Comentário Recente:
    Este script foi um teste de vetores e das funções min() e max().
'''

from random import seed, randint as rint
seed(5)

# Declarando variáveis
vector, vector_lenth, num_min, num_max = [], 20, 0,  100

# Laço de repetição para criar o vetor
for count in range(vector_lenth):
    num = rint(num_min, num_max)
    vector.append(num)
    
print (vector) 
# Separador de Informações
print('-' *30) 

# Declarando Variáveis de leitura
higher = max(vector)
lower = min(vector) 

# Laço de repetição para leitura e output do maior e do menor valor contido no vetor.
for count in range (vector_lenth):
    if (vector[count] == higher):
        print('Na ', count + 1, 'ª posição encontramos o maior valor', higher)
    elif (vector[count] == lower):
        print('Na ', count + 1, 'ª posição encontramos o valor mínimo', lower)