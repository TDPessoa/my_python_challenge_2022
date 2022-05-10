

listageral , lista1 , lista2 , operadores = [] , [] , [] , []

cont , cont2 = 1 , 3

for i in range ( cont2 ):

    while True:

        try:

            ent1 = int( input( f"Digite o {cont}º Valor: " ) )
            lista1.append( ent1 )

            op1 = str( input( f"Digite a {cont}ª operação: " ) )
            operadores.append( op1 )

            ent2 = int( input( f"Digite o {cont}º Valor: " ) )
            lista2.append( ent2 )

            cont += 1

            break

        except ValueError:

            print( "Digite um número válido!" )

        except IndexError:

            print( "Digite um número válido!" )

    if ( operadores[i] == '+' ):

        soma = int( lista1[i] + lista2[i] )
        print( f"\nO valor da soma de {lista1[i]} e {lista2[i]} é {soma}." )
        listageral.append( soma )

    elif ( operadores[i] == '-' ):

        sub = int( lista1[i] - lista2[i] )
        print( f"\nSubtraindo {lista2[i]} de {lista1[i]} encontra-se {sub}." )
        listageral.append( sub )

    elif ( operadores[i] == '*' ):

        prod = int( lista1[i] * lista2[i] )
        print( f"\nO valor do produto de {lista1[i]} e {lista2[i]} é {prod}." )
        listageral.append( prod )

    elif ( operadores[i] == '/' ):

        if lista2[i] == 0:

            print( "Não é possível dividir por 0." )
            listageral.append( -999 )

        else:

            div = int( lista1[i]) / (lista2[i] )
            print( f"\nO valor da divisão de {lista1[i]} por {lista2[i]} é {div:.2f}." )
            listageral.append( div )

print( lista1 , '\n' , operadores , '\n' , lista2 , '\n' , listageral )