"""
Questão 1 - AV1 - Fabio Pessoa, Rachel Vitória, Rodrigo Brito, Thiago Daniel.
Elaborar um algoritmo para armazenar o seguinte texto: “Machine learning é uma área da ciência da computação que
significa aprendizado da máquina. Faz parte do conceito de inteligência artificial, que estuda meios para que máquinas
posam fazer tarefas que seriam executadas por pessoas.”
Utilize o fatiamento de strings para:
a – Extrair as palavras ciência da computação.
b – Inverter as palavras inteligência artificial (de trás para frente).
c – Imprimir somente a 1a frase (até o ponto final) -> Machine learning é uma área da ciência da computação que
significa aprendizado da máquina.
d – Imprimir somente a 2a frase (até o ponto final) -> Faz parte do conceito de inteligência artificial, que estuda
meios para que máquinas posam fazer tarefas que seriam executadas por pessoas.
e – Imprimir somente as vogais da palavra 'executadas' e suas respectivas posições (iniciando do índice 0).
"""

# Declarando a variável <f> contendo a string exigida:
f = "\nMachine learing é uma área da ciência da computação que significa aprendizado da máquina. Faz parte do " \
    "conceito de inteligência artificial, que estuda meios para que máquinas possam fazer tarefas que seriam " \
    "executadas por pessoas."

# Retornando na tela a str completa:
print(f)

# Extrair as palavras -"ciência da computação"- como solicitado pela letra a:
# Como a sequencia de caracteres está nas posições de 31 a 53 da str, usamos <f[30:52]> para acessalos.
print("\n", f[30:52])

# Inverter as palavras "inteligência artificial"
# Estando essas palavras nas posições de 116 a 139, usamos <f[138:115]>
#
print("\n", f[138:115:-1])

# Imprimir somente a primeira frase.
print("\n Primeira frase da string: ", f[:90])

#d) Imprimir somente a segunda frase.
print("\n Segunda frase da string: ", f[91:])

#e) Imprimir as vogais da palavras "executadas" e suas respectivas posições.
p = f[208:219]
print("\n", p)
for i, v in enumerate(p):
    if v == "a" or v == "e" or v == "i" or v == "o" or v == "u" :
        print(f"\n A vogal {v} é a {i+1}ª letra." )