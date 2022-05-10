'''
Comentário Recente:
    Este foi um script que eu fiz com a idéia de experimentar com     \
    fatoriais para entrar com qualquer valor e ele calcular qual é o  \
    fatorial de tal valor. No processo, eu descobri que se eu         \
    entrasse com um valor alto, como acima de 200, o valor final      \
    praticamente fechava a tela do meu celular com digitos desse      \
    fatorial. Então, eu adicionei ao código uma conversão para        \
    binário e fiz um papel de parede em binário para o meu celular. 
'''

# Definindo a função que irá calcular o fatorial
def factorial( valor ) :
    # Variável local
    fatorial_de_valor = 1

    for count in range (2, valor) :
        fatorial_de_valor *= count

    return fatorial_de_valor

# Variáveis globais
uptime, dec_to_bin_check = 0, 0

while ( uptime != 1 ) :
    valor = int(input('Qual valor?')) 
    print(factorial(valor))
    dec_to_bin_check = int(input('Imprimir em binário?')) 

    if ( dec_to_bin_check == 1 ) :
        print(bin(factorial(valor))) 

    uptime = int(input('Mais um?')) 