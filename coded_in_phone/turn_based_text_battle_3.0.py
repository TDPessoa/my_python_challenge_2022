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
hero_hp, enemy_hp = 100, 100

# Defs
    # Turnos:
def turn():
    while True::
        act = int(input('Qual é a sua ação?\nA - Atacar\nB - Bloquear\n' + '-'*20))
        enemy_turn = rint(0, 1)
        
        if (act == 'A' or act == 'a') and (enemy_turn == 1):
            block = rint(0, 5)

            if (block < 1):
                damage = 5 + rint(0, 6)
                print(f'O inimigo tentou levantar seu escudo, mas não conseguiu, você desfere um dano critico de {damage}')
                break

            else:    
                damage = 5 + rint(0, 3) - block
                enemy_hp -= damage
                print(f'O inimigo levanta o escudo em fações de segundo, você causou {damage} de dano.')
                break

        elif (act == 'A' or act == 'a') and (enemy_turn == 0):
            parry_hero = rint(0, 100)
            parry_enemy = rint(0, 100)
            
            if (parry_hero > parry_enemy):
                damage = 5 + rint(0, 5)
                enemy_hp -= damage
                
            
            break

        elif (act == 'B' or act == 'b'):
            block = rint(0, 5)
            if (block < 1):
                print('Você tenta levantar seu escudo, mas não consegue')
            else:
                hero_defense = True
                print('Você levanta seu escudo frações de segundo antes do inimigo começar a se mover.')
            break

        else:
            print('Você se atrapalhou nas várias escolhas disponíveis...')
            break


    # Ações >> Retirado 

    # Feitiços >> retirado
   
    # Elites >> retirado


# Cinco inimigos e um elite >> Retirado

while True:
    turn()

    if (hero_hp <= 0):
        print('Você morreu.')
        break

    elif (enemy_hp <= 0):
        print('Parabens! Você derrotou o inimigo!')
        break

    hero_turn = not hero_turn

print('Obrigado por jogar.')