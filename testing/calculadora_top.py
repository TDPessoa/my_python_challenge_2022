'''calculadora
variavel1
->> int   precisa de um input
operaçao
->> int precisa de um input
variavel2
->> in  precisa de input
resultado
->> condicional da operação


var1 = int(input("Digite o 1º valor:"))

op = int(input("Qual operação você deseja fazer?  '1 = +' '2 = -' '3 = x' '4 = /'"))

var2= int(input('digite o 2º valor:'))

if op ==1:
    result=var1+var2
if op==2:
    result=var1-var2
if op ==3:
    result=var1*var2
if op ==4:
    result=var1/var2

print('o resultado é' ,result)
'''

"""

Calculadora teste
loop
    input unico
    verificação de operação
    split 
    var x
    var y
    result
    
"""
calc = 0
while ( calc != 'end' ):
    while True :
        calc = input(str('Cálculo:'))
        if ( calc.find( '+' ) == False ) or ( calc.find( '-' ) == False ) or \
            ( calc.find( 'x' ) == False ) or ( calc.find( '*' ) == False ) or \
            ( calc.find( '/' ) == False ) :
            print('ERROR')
        else:
            break
    print(calc)

    if ( calc == 'end' ) :
        break