'''
Comentário original:
    Taxa ingresso cinema
Comentário Atual:
    Este foi um script que desenvolvi enquanto tentava explicar como \
    funcionam as condicionais das linguagens de programação para \
    minha namorada, daí o nome do arquivo. ^^
    Como é bem simples, não há mais o que comentar.
'''

while True:
    idade = int(input('Qual a sua idade?'))
    
    if (idade > 0) and (idade <= 21):
        print("Você paga meia entrada.")
        
    elif (idade > 21) and (idade < 65):
        print("Você paga inteira.")
        
    elif (idade >= 65) and (idade < 99):
        print("Você paga meia entrada.")
        
    else:
        print("Idade inválida.")
   
    verify = int(input('Quer continuar? Y = Sim | N = Não'))
    if (verify == "N"):
        break