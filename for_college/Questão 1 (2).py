import random

vetor_x, vetor_y, tam = [], [], 10

# Preenchendo os vetores x e y

for i in range(0, tam, 1):
    vetor_x.append(random.randint(0, 9))
    vetor_y.append(random.randint(0, 9))

interxy = []

# Verificando as Intersessões

for i in range(tam):

    for j in range(tam):

        if (vetor_x[i] == vetor_y[j]):

            ver = vetor_x[i]

            if (ver not in interxy):
                interxy.append(vetor_y[j])

# Imprimindo os vetores

print(vetor_x)
print(vetor_y)

# Ordem Crescente

print(sorted(interxy))

# Ordem Decrescente

interxy.sort(reverse=True)
print(interxy)