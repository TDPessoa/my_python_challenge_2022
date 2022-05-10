"""
Questão 1 - AV1 - Fabio Pessoa, Rachel Vitória, Rodrigo Brito, Thiago Daniel.

Elaborar um algoritmo para armazenar o seguinte texto:

“Machine learning é uma área da ciência da computação que significa aprendizado da máquina. Faz parte do conceito de
 inteligência artificial, que estuda meios para que máquinas possam fazer tarefas que seriam executadas por pessoas.”

Utilize o fatiamento de strings para:

a – Extrair as palavras ciência da computação. ( 30:52 )

b – Inverter as palavras 'inteligência artificial' (de trás para frente). ( 115:138 )

c – Imprimir somente a 1a frase (até o ponto final) -> Machine learning é uma área da ciência da computação que
significa aprendizado da máquina. ( :90 )

d – Imprimir somente a 2a frase (até o ponto final) -> Faz parte do conceito de inteligência artificial, que estuda
meios para que máquinas posam fazer tarefas que seriam executadas por pessoas. ( 91: )

e – Imprimir somente as vogais da palavra 'executadas' e suas respectivas posições (iniciando do índice 0). ( 208:219 )
"""

# Declarando a variavel frase:
frase = 'Machine learning é uma área da ciência da computação que significa aprendizado da máquina. Faz parte do ' \
        'conceito de inteligência artificial, que estuda meios para que máquinas possam fazer tarefas que seriam ' \
        'executadas por pessoas.'

print( frase )

# Letra a:
print( '\n' , frase[30:52] )

# Letra b:
print( '\n' , frase[138:115:-1])

# Letra c:
print( '\n Primeira frase: ' , frase[:90])

# Letra d:
print( '\n Segunda frase: ' , frase[91:])

#Letra e:
palavra = frase[208:219]

print('\n' , palavra)
for i, v in enumerate(palavra):
    if ( v == 'a' ) or ( v == 'e' ) or ( v == 'i' ) or ( v == 'o' ) or ( v == 'u' ):
        print( f'\nA vogal {v} é a { i + 1 }ª letra.')
