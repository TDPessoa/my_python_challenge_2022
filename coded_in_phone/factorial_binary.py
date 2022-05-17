"""Comentário Recente:
    Este foi um script que eu fiz com a idéia de experimentar com     \
    fatoriais para entrar com qualquer valor e ele calcular qual é o  \
    fatorial de tal valor. No processo, eu descobri que se eu         \
    entrasse com um valor alto, como acima de 200, o valor final      \
    praticamente fechava a tela do meu celular com digitos desse      \
    fatorial. Então, eu adicionei ao código uma conversão para        \
    binário e fiz um papel de parede em binário para o meu celular.
Comentário Extra:
    Ao colocar em uma IDE, percebi que o código apresentava um "b"    \
    dentro do resultado final quando utilizava-se da função           \
    built-in bin().
    Como o desafio é para colocar em check meu conhecimento, comecei  \
    a definir uma função própria do código para resolver o problema."""


def factorial(v):  # Função para calcular o fatorial
    fatorial_de_valor = 1  # Variável local
    if (v == 2) or (v == 1) or (v == 0):
        return v

    else:
        for contador in range(2, (v + 1)):
            fatorial_de_valor *= contador

        return fatorial_de_valor


def dec_to_bin(num):  # Função para converter decimal para binário.
    binario = ''  # String que conterá o resultado.
    contador = 0  # Contador para determinar o maior expoente de dois.

    while True:
        # Verificador para saber se 2 exponenciado por 'contador' é \
        # maior que 'num'.
        if 2**contador > num:
            break

        # Se o verificador for 'False', o contador será aumentado \
        # para a próxima verificação.
        contador += 1

    # Loop para fazer a concatenação e adicionar a str('binario')    
    for i in range((contador - 1), -1, -1):
        # Na condição, str('0') é concatenado ao 'binario'.
        if (2**i > num) or (num == 0):
            binario += '0'

        # Nesta condição, o 'num' é maior ou igual a int(2**i), \
        # portanto, a casa binaria em questão recebe um str('1').
        elif 2**i <= num:
            binario += '1'
            num -= 2 ** i

    return binario

# Código global um laço while para repetição de operações
while True:
    # Outro laço while para verificar se 'valor' é positivo
    while True:
        valor = int(input('Qual valor?'))

        if valor < 0:
            print('Valor precisa ser positivo.')

        # Execução de 'factorial()' e quebra do loop interno
        else:
            print(factorial(valor))
            break

    # Condicional para optar em processar o 'factorial()' em binario
    if int(input('Quer converter para binario? Y - Sim')) == 'Y':
        # Execução de 'dec_to_bin()'
        print(dec_to_bin(factorial(valor)))

    # Condicional para optar 
    if int(input('Quer repetir? Y - Sim')) == 'Y':
        pass
    else:
        print('Ok, tchau!')
        break
