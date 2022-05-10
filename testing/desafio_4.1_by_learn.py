"""
Número mágico:
Definir uma valor de 1 a 5

input de valores

Verificação e resposta se o valor de input está acima ou abaixo do definido
"""

def main():
    n_plateia = 2
    adiv_magico = int(input('O seu número é:'))
    if adiv_magico == n_plateia :
        print('Correto!')
    elif adiv_magico > n_plateia :
        print('É menor.')
    else:
        print('É maior.')

def main_b():
    import random
    n_plateia = random.randint(0,100)
    while True:
        n_adiv = int(input('Qual é o valor aleatório?'))
        if n_adiv == n_plateia :
            print('Correto')
            break
        else:
            if n_plateia > n_adiv :
                print('É maior!')
            elif n_plateia < n_adiv :
                print('É menor!')


main_b()
