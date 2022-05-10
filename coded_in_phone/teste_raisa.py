'''
Taxa ingresso cinema
'''
x = 1
while x == 1:
    idade = int(input('Qual a sua idade?'))
    
    if ( idade > 0 ) and idade<21:
        print("Você paga meia entrada.")
        
    elif idade>21 and idade<65:
        print("Você paga inteira.")
        
    elif idade > 65 and idade < 99:
        print("Você paga meia entrada.")
        
    else:
        print("Idade inválida.")
   
    x = int(input('Quer continuar? 1 - Sim e 2 - Não.'))