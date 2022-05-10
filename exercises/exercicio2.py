'''Elaborar um algoritmo que preencha 3 vetores de 10 posições para a produção de uma calculadora. Os 2
primeiros vetores receberão valores numéricos inteiros (operandos) e o terceiro vetor receberá os
operadores (+, – , * e /), representando as operações de adição, subtração, multiplicação e divisão,
respectivamente. O algoritmo deverá fazer a conta e gravar o resultado em um quarto vetor. Todos os
vetores deverão ser impressos.
Obs: Fazer a proteção de dados no terceiro vetor, isto é, só é possível aceitar os operadores +, – , * e /.
Contornar o erro de divisão por zero caso ocorra a operação (/) com o denominador 0, acrescentando
àquela posição o valor -999.'''

#listas
listageral = []
lista1 = []
lista2 = []
operadores = []


#contadores
cont = 1

cont2 = 3


#inicio do laço
while (cont2 <= 3):
    #tratamento de erro para quando não for digitado um número inteiro ou valido
    #try:
        #repetição
    for i in range(cont2):
        #variavel de entrada do 1º numero inteiro e adiciona o numero na ultima posição a lista
        ent1 = int(input(f"Digite o {cont}º Valor: "))
        lista1.append(ent1)

        #variavel de entrada da operação e adiciona o operador na ultima posição a lista
        op1 = str(input(f"Digite a {cont}ª operação: "))
        operadores.append(op1)

        #variavel de entrada do 2º número inteiro e adiciona o numero na ultima posição a lista
        ent2 = int(input(f"Digite o {cont}º Valor: "))
        lista2.append(ent2)

        if operadores[i] == '+':
            soma = int(lista1[i] + lista2[i])
            print(f"\nO valor da soma de {lista1[i]} e {lista2[i]} é {soma}")
            listageral.append(soma)

        elif operadores[i] == '-':
            sub = int(lista1[i] - lista2[i])
            print(f"\nO valor da subtração de {lista1[i]} e {lista2[i]} é {sub}")
            listageral.append(sub)

        elif operadores[i] == '*':
            prod = int(lista1[i] * lista2[i])
            print(f"\nO valor do produto de {lista1[i]} e {lista2[i]} é {prod}")
            listageral.append(prod)

        elif operadores[i] == '/':
            if lista2[i] == 0:
                print("Não é possível dividir por 0")
                listageral.append(-999)
            else:
                div = int(lista1[i]) / (lista2[i])
                print(f"\nO valor da divisão de {lista1[i]} e {lista2[i]} é {div:.2f}")
                listageral.append(div)

        elif operadores[i] != '/' or operadores[i] != '*' or operadores[i] != '-' or operadores[i] != '+':
            print("Digite uma operação valida!")
            cont -= 1

            lista1.pop(-1)
            lista2.pop(-1)
            operadores.pop(-1)

        cont += 1
        cont2 += 1
'''
    except ValueError:
        print("Digite um número válido!")
        cont2 -= 1


    except IndexError:
        print("Digite um número válido!")
        cont2 -= 1
'''




print(cont)
print(cont2)

print(listageral)
print(lista1)
print(lista2)
print(operadores)