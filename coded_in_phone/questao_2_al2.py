'''
Comentário original:
    Dada uma matriz 8x8 de números inteiros, efetuar as seguintes \
    operações:
    a) Apresentar a quantidade de números primos existentes na matriz;
    b) Comparar o somatório dos números pares da diagonal principal \
    com o somatório dos números ímpares da coluna 2 e informar se é \
    maior, menor ou igual.
'''

from random import randint as rint
random.seed(2)

# Definindo as funções necessárias 
def is_prime( num ) :
    if ( num > 2 ) :
        for count in range ( 2 , num ) :
            if ( num % count == 0 ) :
                result = False
                break
            
            else :
                result = True
        
        return result
    
    elif ( result == 2 ) :
        return True
    
    else :
        return False

def is_even( num ) :
    if ( num % 2 == 0 ) :
        return True 
    
    else :
        return False

# Declaração de variaveis globais
matrix, lenth, prime_count = [], 8, 0
main_diag_evens_sum, sec_coll_odds_sum = 0, 0

# Gerando a matriz
for i in range (lenth):
    row = []
    for j in range (lenth):
        num = rint(0, 999)
        row.append(num)
   
    matrix.append(row)


# Imprimindo a matriz e coleta de dados
for i in range(lenth):
    for j in range(lenth):
        # Verificador se está na diagonal principal e se é par
        if (i == j) and (is_even(matrix[i][j]) == True):
            # Valor adicionado à soma de pares na diagonal principal
            main_diag_evens_sum += matrix[i][j] 

        # Verificando se está na segunda coluna(index 1) e se não é par
        elif (j == 1) and (is_even(matrix[i][j]) == False):
            # Valor adicionado á soma de ímpares da coluna 2
            sec_coll_odds_sum += matrix[i][j]
        
        # Verificando se o valor atual é um número primo
        if (is_prime(matrix[i][j]) == True):
            # Adicionando ao contador de numeros primos
            prime_count += 1
        
        # Output do valor atual com tabulação 
        print(f'{matrix[i][j]:^3}', end = '\t')
    
    # Quebra de linha para recomeçar o loop
    print('\n')

# Output da coleta de dados:
    
    # Quantidade de numeros primos
print( 'A matriz possui', prime_count , 'números primos.') 

    # Verificadores para adequar a mensagem de saída ao resultado
if (main_diag_evens_sum > sec_coll_odds_sum) :
    print('A soma dos números pares da diagonal principal é maior que \
        a soma dos impares da 2ª coluna.')

elif  (main_diag_evens_sum == sec_coll_odds_sum) :
    print('A soma dos números pares da diagonal principal é igual a \
        soma dos impares da 2ª coluna.') 

else :
    print('A soma dos números pares da diagonal principal é menor que \
        a soma dos impares da 2ª coluna.') 