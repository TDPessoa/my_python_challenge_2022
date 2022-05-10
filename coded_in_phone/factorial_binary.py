def factorial( n ) :
    x = 1
    for c in range ( 2 , n ) :
        x *= c
    return x


d , e = 0 , 0
while ( d != 1 ) :
    f = int( input( 'Qual valor?' ) ) 
    print( factorial( f ) )
    e = int( input( 'Imprimir em binário?' ) ) 
    if ( e == 1 ) :
        print( bin( factorial( f ) ) ) 
    d = int( input( 'Mais um?' ) ) 