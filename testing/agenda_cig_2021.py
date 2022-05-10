'''
Comentário original:
    Programa para calcular aleatoriamente minha agenda para os dias que
        ficarei sem cigarros

Comentário de edição:
    Esta foi uma tentativa frustrada de regrar meus dias para que eu 
        tivesse um método de cesssar meu hábito tabagista.
    Irei descontinuar este arquivo, após coloca-lo nos padrões de  
        digitação e comentários.
        
    A idéia seria gerar quinze semanas(as quais faltavam para terminar 
        o ano e definir 12 horas que eu ficaria sem fumar, esse horário
        poderia ser o primeiro, segundo, ... , décimo quarto "meio dia"
        dessa semana. Para cada mês que fosse progredindo o sistema, 
        era adicionado mais um bloco de 12 horas para a semana. 
        Em tese, ao final do período definido, eu iria fazer outro 
        script para o ano de 2022 e seguiria a mesma linha de 
        raciocínio.
'''

from random import randint as rint
random.seed(920008966)

def vou_parar_de_fumar_2022():
    # Laço de repetição para a definição das 15 semanas
    for semana in range (0 , 16):

        # Condicional para definir se está no primeiro mês, gerando 
        # somente um bloco de 12h para a agenda
        if (semana <= 4):
            bloco_1 = rint(1, 14)
            print(f"{semana}|{bloco_1}")

        # Condicional para o segundo mês, gerando dois blocos por 
        # semana.
        elif (semana > 4) and (semana <= 8):
            if (semana == 5):
                # Separador de linhas para dividir os meses
                print("--"*40)

            bloco_1, bloco_2 = rint(1, 14), rint(1, 14)
            print(f"{semana}|{bloco_1} + {bloco_2}")

        # Terceiro mês, três blocos por semana
        elif (semana > 8) and (semana <= 13):
            # Separador de meses
            if (semana == 9)
                print("--"*40)

            bloco_1, bloco_2, bloco_3 = rint(1, 14), rint(1, 14), \
                                        rint(1, 14)
            print(f"{semana}|{bloco_1} + {bloco_2} + {bloco_3}")

        # Quarta semana, quatro blocos
        else:
            # Separador
            if (semana == 13):
                print("--"*40)
                
            bloco_1, bloco_2, bloco_3, bloco_4 = rint(1, 14), \
                                                    rint(1, 14), \
                                                    rint(1, 14), \
                                                    rint(1, 14)
            print(f"{semana}|{bloco_1} + {bloco_2} + \
                    {bloco_3} + {bloco_4}")

vou_parar_de_fumar_2022()