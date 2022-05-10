#Odds test randint w/ count

import random

a, b, c, d, e, z = 0, 0, 0, 0, 0, 304972
for cc in range ( 0, 100):
    for x in range ( 0, 100 ):
        #random.seed(z) 
        y = random.randint( 0, 4 )
        #print(y) 
        if ( y == 0 ):
            a += 1
        elif ( y == 1 ):
            b += 1
        elif ( y == 2 ):
            c += 1
        elif ( y == 3 ):
            d += 1
        elif ( y == 4 ):
            e += 1
    #print('seed=', z) 
    print( a, '% of a' )
    print( b, '% of b' )
    print( c, '% of c' )
    print( d, '% of d' )
    print( e, '% of e' )
    print(20*'-')
    a, b, c, d, e = 0, 0, 0, 0, 0
    z += 1
