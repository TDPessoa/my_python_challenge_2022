import random

count = 0

for c in range ( 10 ) :

	x , y , z = random.randint( 1 , 100 ), random.randint( 1 , 100 ), random.randint( 1 , 100 )

	if ( z%3 == 0 ) :

		res = x + y
		print( 'Quanto é' , x , '+' , y , '?' )

	elif ( z%3 == 1) :

		if ( x > y ) :
			res = x - y
			print( 'Quanto é' , x , '-' , y , '?' )

		else:
			res = y - x
			print( 'Quanto é' , y , '-' , x , '?' )
		
	else :

		res = x * y
		print( 'Quanto é' , x , 'x' , y , '?' )

	while True :

		a = int( input( ) )

		if ( a == res ) :

			print( 'Correto!!!' )
			break

		else: 

			count += 1
			print( 'Errado :( \n Tenta de novo...' )

	print( '-' * 30 )

if ( count == 0 ):

	print( 'Parabéns! Zero erros!' )

elif ( count > 0 ) and ( count <= 10 ) :

	print( 'Quase lá, só errou' , count , 'vezes!')

elif ( count > 10 ) :

	print( 'Vixe... Errou' , count , 'vezes, continue praticando.')