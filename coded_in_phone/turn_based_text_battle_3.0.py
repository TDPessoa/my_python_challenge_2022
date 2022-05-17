"""Comentário Recente:
Este é um script que sugriu com meus colegas e faculdade nos \
primeiros contatos com python, queriamos criar um joguinho de \
texto turn-based e ajudou bastante a desenvolver minhas praticas \
e aprimorar minha abordagem nos codigos.
Como ele não está operacional no momento, irei tentar concluir e \
deixar os defs de acordo, mas tenho certeza que ele está melhor em \
outra pasta do diretório, se não estiver, irei move-lo para a WIP."""

# Imports necessários:
from random import randint as rint

# Declarando variáveis globais:
hero_hp, enemy_hp = 100, 100


# Função que irá operar os turnos
def turn():
    global hero_hp
    print(('-' * 20) + f'\nSua vida = {hero_hp}\nVida do inimigo = {enemy_hp}')
    act = str(input('Qual é a sua ação?\n\tA - Atacar\n\tB - Bloquear\n' + ('-' * 20) + '\n'))
    enemy_turn = rint(0, 1)

    if act == 'A':
        attack(enemy_turn)

    elif act == 'B':
        defense(enemy_turn)

    else:
        hero_hp -= 5
        print(f'Você se atrapalha entre tantas ações, tropeça e perde 5 pontos de vida.')


def attack(n):
    global hero_hp, enemy_hp
    hero_atk, enemy_atk = (5 + rint(0, 5)), (5 + rint(0, 5))
    if n == 0:
        print('Você e o inimigo avançam ao mesmo instante.')

        if hero_atk > enemy_atk:
            enemy_hp -= hero_atk
            print(f'Porém, você foi mais rápido, o inimigo perde {hero_atk} de vida.')

        elif hero_atk < enemy_atk:
            hero_hp -= enemy_atk
            print(f'Porém, o inimigo foi mais rápido, você perde {enemy_atk} de vida.')

        else:
            print(f'Porém, uma arma apara a outra, ninguém se feriu.')

    else:
        enemy_def = rint(0, 5)
        print('O inimigo começa a levantar o escudo frações de segundo antes de você atacar.')

        if enemy_def == 0:
            enemy_hp -= hero_atk
            print(f'Ele não consegue levantar a tempo e recebe {hero_atk} de dano a vida.')

        else:
            enemy_hp -= (hero_atk - enemy_def)
            print(
                f'Sua arma é bloqueada pelo escudo do inimigo mas, ainda assim, causa {hero_atk - enemy_def} de dano.')


def defense(n):
    global hero_hp
    hero_def, enemy_atk = rint(0, 5), (5 + rint(0, 5))
    if n == 0:
        if hero_def == 0:
            hero_hp -= enemy_atk
            print(f'Você tenta levantar seu escudo, mas falha, recebendo {enemy_atk} de dano.')
        else:
            hero_hp -= (enemy_atk - hero_def)
            print(f'Você levantou seu escudo, mas recebeu {enemy_atk - hero_def} de dano.')

    else:
        print('Ambos levantaram o escudo, que embaraoso...')


while True:
    turn()

    if hero_hp <= 0:
        print('Você morreu.')
        break

    elif enemy_hp <= 0:
        print('Parabens! Você derrotou o inimigo!')
        break

print('Obrigado por jogar.')
