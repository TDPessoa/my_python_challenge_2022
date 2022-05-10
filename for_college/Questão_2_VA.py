# listas
listageral = []
lista1 = []
lista2 = []
operadores = []

# contadores
cont, cont2 = 1, 10

print("*" * 60)
print(
    f"CALCULADORA PYTHON\nPARA SOMA USE '+'\nPARA SUBTRAÇÃO USE '-'\nPARA MULTIPLICAÇÃO USE '*'\nPARA DIVISÃO USE '/'")
print("*" * 60)

for i in range(cont2):
    while True:
        try:
            # variavel de entrada do 1º numero inteiro e adiciona o numero na ultima posição a lista
            ent1 = int(input(f"Digite o {cont}º Valor: "))
            lista1.append(ent1)

            # variavel de entrada da operação e adiciona o operador na ultima posição a lista
            op1 = str(input(f"Digite a {cont}ª operação: "))
            operadores.append(op1)

            # variavel de entrada do 2º número inteiro e adiciona o numero na ultima posição a lista
            ent2 = int(input(f"Digite o {cont}º Valor: "))
            lista2.append(ent2)

            break
        # tratamentos de erros de indexação e valor
        except ValueError:
            print("Digite um número válido!")
        except IndexError:
            print("Digite um número válido!")

    # condições para opereção
    if operadores[i] == '+':
        soma = int(lista1[i] + lista2[i])
        print(f"\nO valor da soma de {lista1[i]} e {lista2[i]} é {soma}")
        listageral.append(soma)
        print("*" * 60)

    elif operadores[i] == '-':
        sub = int(lista1[i] - lista2[i])
        print(f"\nO valor da subtração de {lista1[i]} e {lista2[i]} é {sub}")
        listageral.append(sub)
        print("*" * 60)

    elif operadores[i] == '*':
        prod = int(lista1[i] * lista2[i])
        print(f"\nO valor do produto de {lista1[i]} e {lista2[i]} é {prod}")
        listageral.append(prod)
        print("*" * 60)

    elif operadores[i] == '/':
        # tratamento de erro divisão por '0'
        if lista2[i] == 0:
            print("Não é possível dividir por 0")
            listageral.append(-999)
            print("*" * 60)
        else:
            div = int(lista1[i]) / (lista2[i])
            print(f"\nO valor da divisão de {lista1[i]} e {lista2[i]} é {div:.2f}")
            listageral.append(div)
            print("*" * 60)
    # tratamento de erros para digitação de operadores fora de padrão
    elif operadores[i] != '/' or operadores[i] != '*' or operadores[i] != '-' or operadores[i] != '+':
        print("Digite uma operação valida!")
        cont -= 1
        print("*" * 60)

        lista1.pop(-1)
        lista2.pop(-1)
        operadores.pop(-1)

    cont += 1
    cont2 += 1


print(f"\n{lista1}\n{operadores}\n{lista2}\n{listageral}")

print(f"\nCalculadora python by: \nFabio Pessoa\nRachel Vitória\nRodrigo Brito\nThiago Daniel.")


