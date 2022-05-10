f = "\nMachine learing é uma área da ciência da computação que significa aprendizado da máquina. Faz parte do conceito de inteligência artificial, que estuda meios para que máquinas possam fazer tarefas que seriam executadas por pessoas."
print(f)

#a) Extrair as palavras "ciência da computação".
print("\na) ", f[30:52])

#b) Inverter as palavras "inteligência artificial"
print("\n", f[138:115:-1])


#c) Imprimir somente a primeira frase.
print("\nc) Primeira frase da string: ", f[:90])

#d) Imprimir somente a segunda frase.
print("\nd) Segunda frase da string: ", f[91:])

#e) Imprimir as vogais da palavras "executadas" e suas respectivas posições.
p = f[208:219]
print("\ne)", p)
for i, v in enumerate(p):
    if v == "a" or v == "e" or v == "i" or v == "o" or v == "u" :
        print(f"\n Vogal {v} na posição {i}." )