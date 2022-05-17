'''Comentário Original:
    Odds test randint w/ count
Comentário Recente:
    Este foi um script simple que desenvolvi para testar as precisões \
    de probabilidade de várias seeds em random, pois planejava \
    implementar um sistema de chances aleatórias em um programa, e \
    queria saber se utilizando um verificador, eu iria conseguir uma \
    seed específica que faria com que seus randints tivessem \
    probabilidades iguais de serem "rolados".'''

from random import randint as rint

# Declarando variáveis para guardar as quantidades que cada possível \
# roll aconteceu em dado loop
count_one, count_two, count_three = 0, 0, 0
count_four, count_five = 0, 0
num_seed = 0

# Serão feitas cem colétas dentro de cem seeds
for count in range (0, 100):
    for internal_count in range (0, 100):
        # A seed é declarada com 1 valor adicionado a cada coleta
        random.seed(num_seed) 
        num = rint(0, 4)

         
        if (num == 0):
            count_one += 1

        elif (num == 1):
            count_two += 1

        elif (num == 2):
            count_three += 1

        elif (num == 3):
            count_four += 1

        elif (num == 4):
            count_five += 1

    # Output das informações
    print('seed=', z) 
    print(count_one, '% ' + 'of ones')
    print(count_two, '% ' + 'of twos')
    print(count_three, '% ' + 'of threes')
    print(count_four, '% ' + 'of fours')
    print(count_five, '% ' + 'of fives')
    print(20*'-')

    # Declarando as variáveis para o estado inicial
    count_one, count_two, count_three = 0, 0, 0
    count_four, count_five = 0, 0

    # Avançando a seed
    num_seed += 1