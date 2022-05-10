'''
Dada	uma	matriz	8x8	de	números	inteiros,	efetuar	as 
seguintes	operações:
a) Apresentar	a	quantidade	de	números	primos	existentes	
na	 matriz;
b)	 Comparar	 o	 somatório	 dos	 números	 pares	 da	 
diagonal	 principal	 com	 o	 somatório	 dos	 números	
ímpares	da	coluna	2	e	informar	se	é	maior,	menor	ou	igual.
'''

import random

#random.seed(2)

# Definição das funções necessárias 
def is_prime( n ) :
    
    if ( n > 2 ) :
        
        for c in range ( 2 , n ) :
            
            if ( n % c == 0 ) :
                y = False
                break
            
            else :
                y = True
        
        return y
    
    elif ( n == 2 ) :
        return True
    
    else :
        return False

def is_even( n ) :
    
    if ( n % 2 == 0 ) :
        return True 
    
    else :
        return False

# Declaração de variaveis base
matriz , tam , prime_count = [] , 8 , 0
diag_princ_even , col_2_odd = 0 , 0

# Gerando a matriz
for i in range ( tam ) :
    
    linha = []
    
    for j in range ( tam ) :
        num = random.randint( 0 , 999 )
        linha.append( num )
   
    matriz.append( linha )


# Imprimindo a matriz e coleta de dados
for i in range ( tam ):
   
    for j in range ( tam ):
       
        if ( i == j ) and ( is_even( matriz[i][j] ) == True ) :
            diag_princ_even += matriz[i][j] 
        
        elif ( j == 1 ) and ( is_even( matriz[i][j] ) == False ) :
            col_2_odd += matriz[i][j]
      
        if ( is_prime( matriz[i][j] ) == True ) :
            prime_count += 1
        
        print( f'{matriz[i][j]:^3}' , end = '\t' )
  
    print('\n')

print( 'A matriz possui', prime_count , 'números primos.') 

if ( diag_princ_even > col_2_odd ) :
    print( 'A soma dos números pares da diagonal principal é maior que a soma dos impares da 2ª coluna.')
elif ( diag_princ_even == col_2_odd ) :
    print( 'A soma dos números pares da diagonal principal é igual a soma dos impares da 2ª coluna.' ) 
else :
    print( 'A soma dos números pares da diagonal principal é menor que a soma dos impares da 2ª coluna.' ) 
