'''
Comentário Recente:
    Este é um script que sugriu com meus colegas e faculdade nos \
    primeiros contatos com python, queriamos criar um joguinho de \
    texto turn-based e ajudou bastante a desenvolver minhas praticas \
    e aprimorar minha abordagem nos codigos.
    Como ele não está operacional no momento, irei tentar concluir e \
    deixar os defs de acordo, mas tenho certeza que ele está melhor em \
    outra pasta do diretório, se não estiver, irei move-lo para a WIP.
'''
# Imports necessários:
from random import randint as rint

# Declarando variáveis globais:
hero_hp, hero_base_attack = 100, 5
enemy_hp, enemy_base_attack = 100, 5
hero_turn, hero_defense, enemy_defense = True, False, False

# Defs
    # Turnos:
def turn():
    if (hero_turn == True):
        act = int(input('Qual é a sua ação? \nA - Atacar \
            \nB - Bloquear\n' + '-'*20))
        
        if (hero_turn == 'A') and (enemy_defense == True):
            damage = hero_base_attack + rint(0, 5) - enemy_block
            enemy_hp -= damage
            print(f'Você desfere um golpe contra o escudo do inimigo, \
                causando {damage} de dano à sua saúde.')

        elif (hero_turn == 'A') and (enemy_defense == False):
            damage = hero_base_attack + rint(0, 5)
            enemy_hp -= damage
            print(f'Você desfere um golpe contra o inimigo, causando \
                {damage} de dano à sua saúde.')

        elif (hero_turn == 'B'):

            block = rint(0, 5)
            print("Você levanta seu escudo frações de segundo antes \
                do inimigo começar a se mover.")

        else:


    else:
        enemy_turn = rint(0, 1)
        if (enemy_turn == 0) and (hero_defense == True):
            damage = hero_base_attack + rint(0, 5) - enemy_block
            enemy_hp -= damage
            print(f'Você desfere um golpe contra o escudo do inimigo, \
                causando {damage} de dano à sua saúde.')
        elif (hero_turn == 1) and (enemy_defense == False):
            damage = hero_base_attack + rint(0, 5)
            enemy_hp -= damage
            print(f'Você desfere um golpe contra o inimigo, causando \
                {damage} de dano à sua saúde.')

        elif (hero_turn == 2) and (enemy_defense == False):
            block = rint(0, 5)
            print("Você levanta seu escudo frações de segundo antes \
                do inimigo começar a se mover.")

    # Ações >> Retirado 

    # Feitiços >> retirado
   
    # Elites >> retirado


# Cinco inimigos e um elite
