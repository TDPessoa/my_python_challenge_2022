'''
Comentário Recente:
    Este script foi uma tentativa de desenvolver um gerador aleatório \
    e um verificador de quadros de sudoku para um dia ser um jogo de \
    fato.
    Desenvolver esse script é uma vontade que estava além do meu \
    conhecimento e continua até hoje, quabrei a cabeça de mais para \
    fazer funcionar, mas os bugs sempre apareciam diferentes, até que \
    eu desisti... Por ora.
'''

import random

def sudokuprint():
    
    for a in range ( 9 ):
        
        for b in range ( 9 ):
            
            print( sudoku[a][b], end='\t')
        
        print('\n') 

'''def sudokucheck() :
    
    for a in range ( 9 ):
        
        for b in range ( 9 ) :'''

sudoku = []
y = 0

for a in range ( 9 ) :
    
    row = []
    
    for b in range ( 9 ) :
        
        while True:
            
            x = random.randint( 0, 9)
            if ( x == 0 ) :
                row.append(x)
                break
                
            else:
                for c in range (a) :
                    if x == sudoku[c][b]:
                        y += 1 
            
                if (( x not in row ) and ( x != 0 ) 
                and ( y == 0)) :
                    row.append(x)
                    break
                y = 0
            
    sudoku.append(row)
    '''if a > 0:
        
        for c in range ( a ) :
            
            for d in range '''

sudokuprint() 