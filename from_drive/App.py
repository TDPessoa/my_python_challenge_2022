'''

Programa Atendimento - Henrique Lanches
Desenvolvedores: Rachel Nunes, Rodrigo Brito e Thiago Pessoa

Código apresentado ao curso Tecnólogo em Sistemas de informação,
da Faculdade de Educação Tecnológica do Estado do Rio de Janeiro,
para obtenção de nota

Orientador: Cláudio

'''

# Variável para loop do horário de serviço
a=0
# Variável para dar ordem aos pedidos
c=0
# Variável para armazenar os itens do dia
d=[]
# Variável para armazenar o valor total do pedido
total=0
# Variável para armazenar o valor total do caixa
caixa=0
# Variável para dar ordem aos itens de um pedido
g=0

# Definição para a entrada da variedade
def sabor():
    if (sb==1):
        d.append("Carne")
    elif(sb==2):
        d.append("Frango")
    elif(sb==3):
        d.append("Contra-Filé")
    elif(sb==4):
        d.append("Calabresa")
    elif(sb==5):
        d.append("Picanha")
    elif(sb==6):
        d.append("Filé de Frango")
    elif (sb ==7):
        d.append("Queijo Prato")
    elif (sb ==8):
        d.append("Queijo Cheddar")
    elif (sb ==9):
        d.append("Queijo Provolone")
    elif (sb ==10):
        d.append("Linguiça")
    elif (sb ==11):
        d.append("Salsisha")
    elif (sb ==12):
        d.append("Pequeno")
    elif (sb ==13):
        d.append("Médio")
    elif (sb ==14):
        d.append("Grande")
    elif (sb ==15):
        d.append("Misto")

# Definição de separador de tela. comanda cozinha / operação do caixa

def sep():
    print("-"*30)

# Definição sabor suco

def suco():
    sb=int(input("Qual é sabor do suco? "))
    if(sb==1):
        d.append("Morango")
    elif(sb==2):
        d.append("Maracujá")
    elif(sb==3):
        d.append("Abacaxi")
    elif(sb==4):
        d.append("Abacaxi com Hortelã")
    elif(sb==5):
        d.append("Cupuaçu")
    elif(sb==6):
        d.append("Graviola")
    elif(sb==7):
        d.append("Goiaba")
    elif(sb==8):
        d.append("Manga")

# Inicio do loop de serviço

while(a==0):
    sep()
    c+=1
    # Variável para loop de pedido em andamento
    b=0
    while (b==0):
        g+=1
        pdd=int(input("\nDigite o número do {}º item: ".format(g)))
        #loop dos sanduiches
        if(pdd==1):
            d.append("\nX-Tudo")
            sb = int(input("Qual é o tipo de carne? "))
            sabor()
            if(sb==1):
                preco=7.5
            elif(sb==2):
                preco=8
            elif(sb==3):
                preco=13
            elif(sb==4):
                preco=8.5
            elif(sb==5):
                preco=10
            elif(sb==6):
                preco=11
        elif(pdd==2):
            d.append("\nX-Cheddar")
            sb = int(input("Qual é o tipo de carne? "))
            sabor()
            if(sb==1):
                preco=8.5
            elif(sb==2):
                preco=9
            elif(sb==3):
                preco=14.5
            elif(sb==4):
                preco=9.5
            elif(sb==5):
                preco=11
            elif(sb==6):
                preco=12.5
        elif(pdd==3):
            d.append("\nHamburguer")
            sb = int(input("Qual é o tipo de carne? "))
            sabor()
            if(sb==1):
                preco=6
            elif(sb==2):
                preco=6.5
            elif(sb==3):
                preco=11
            elif(sb==4):
                preco=6.5
            elif(sb==5):
                preco=8.5
            elif(sb==6):
                preco=9
        elif(pdd==4):
            d.append("\nX-Bacon")
            sb = int(input("Qual é o tipo de carne? "))
            sabor()
            if(sb==1):
                preco=8
            elif(sb==2):
                preco=8.5
            elif(sb==3):
                preco=13
            elif(sb==5):
                preco=10.5
            elif(sb==6):
                preco=11.5
        elif(pdd==5):
            d.append("\nX-Especial")
            sb = int(input("Qual é o tipo de carne? "))
            sabor()
            if(sb==1):
                preco=9.5
            elif(sb==2):
                preco=10
            elif(sb==3):
                preco=17.5
            elif(sb==4):
                preco=10.5
            elif(sb==5):
                preco=12.5
            elif(sb==6):
                preco=14.5
        elif(pdd==6):
            d.append("\nX-Marmita")
            sb = int(input("Qual é o tipo de carne? "))
            sabor()
            if(sb==1):
                preco=13
            elif(sb==2):
                preco=13.5
            elif(sb==4):
                preco=14
            elif(pdd==5):
                preco=17
        elif(pdd==7):
            d.append("\nArtesanl 150g")
            sb = int(input("Qual é o tipo de queijo? "))
            sabor()
            if(sb==7):
                preco=11
            elif(sb==8):
                preco=11.5
            elif(sb==9):
                preco=12.5

        elif(pdd==8):
            d.append("\nArtesanal 300g")
            sb = int(input("Qual é o tipo de queijo? "))
            sabor()
            if(sb==7):
                preco=17
            elif(sb==8):
                preco=17.5
            elif(sb==9):
                preco=18.5

        elif(pdd==9):
            d.append("\nPão com Linguiça")
            preco=9

        elif(pdd==10):
            d.append("\nFilé Árabe")
            preco=11

        elif(pdd==11):
            d.append("\nLombo Suíno")
            preco=9.5

        elif(pdd==12):
            d.append("\nFit")
            preco=9

        elif(pdd==13):
            d.append("\nCachorro Quente")
            sb = int(input("De linguiça ou salsicha? "))
            sabor()
            if(sb==10):
                preco=6
            elif(sb==11):
                preco=5.5

        elif(pdd==14):
            d.append("\nBatata Frita Comum")
            sb = int(input("Qual é o tamanho? "))
            sabor()
            if(sb==13):
                preco=15
            elif(sb==14):
                preco=20

        elif(pdd==15):
            d.append("\nBatata Frita Especial")
            sb = int(input("Qual é o tamanho? "))
            sabor()
            if(sb==13):
                preco=20
            elif(sb==14):
                preco=25

        elif(pdd==16):
            d.append("\nBaurú")
            sb = int(input("Qual é a carne? "))
            sabor()
            if(sb==1):
                preco=34
            elif(sb==2):
                preco=32
            elif(sb==15):
                preco=36

        elif(pdd==17):
            d.append("\nMisto Quente")
            preco=5

        elif(pdd==18):
            d.append("\nTaça de Açaí")
            sb = int(input("Qual é o tamanho? "))
            sabor()
            if(sb==12):
                preco=6
            elif(sb==14):
                preco=8.5

        #loop de bebidas

        elif(pdd==19):
            d.append("\nSuco")
            suco()
            preco=5

        elif(pdd==20):
            d.append("\nAo Leite")
            suco()
            preco=6

        elif(pdd==21):
            d.append("\nRefrigerante 2L")
            preco=9

        elif(pdd==22):
            d.append("\nRefrigerante Lata")
            preco=4.5

        elif(pdd==23):
            d.append("\nGuaraviton")
            preco=4.5

        elif(pdd==24):
            d.append("\nIce Tea")
            preco=4

        elif(pdd==25):
            d.append("\nSchweppes Citrus")
            preco=5

        elif(pdd==26):
            d.append("\nMate Leão")
            preco=4

        elif(pdd==27):
            d.append("\nH2Oh!")
            preco=5

        elif(pdd==28):
            d.append("\nÁgua sem gás")
            preco=2

        elif(pdd==29):
            d.append("\nGuaravita")
            preco=2

        esp=str(input("Pedido Especial? (S/N) "))

        #verificado de adicionais e especialidade

        if(esp=="s"):
            adc=int(input("Quantos adicionais? "))
            espc=str(input("Especial como? "))
            d.append(espc)
            total+=preco+(adc*2)

        else:
            total+=preco
        fpdd=str(input("\nEncerrar pedido? (S/N) "))

        if(fpdd=="s"):
            sep()
            print("Pedido nº", c)
            for i in d:
                print(i)
            sep()
            print("\nO Total do pedido é R${:.2f}".format(total))
            caixa+=total
            total=0
            d=[ ]
            b=1
            g=0

    fa=str(input("Finalizar o dia? (S/N) "))
    if(fa=="s"):
        print("\nO total do caixa é R${:.2f}".format(caixa))
        a=1
    else:
        b=0
print("\n")
sep()
print("      Fim dos Trabalhos!      ")
sep()