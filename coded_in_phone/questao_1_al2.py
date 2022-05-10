import random

random.seed(2)

vet_x, tam, x_min, x_max = [], 20, - 5, 30

for c in range ( tam ) :
    num = random.randint( x_min , x_max )
    vet_x.append( num )
    
print (vet_x) 

print('-' *30) 

x = max(vet_x)
y = min(vet_x) 

for c in range ( tam ) :
    if ( vet_x[c] == x ) :
        print('Na ', c + 1, 'ª posição encontramos o valor máximo',x)
    elif (vet_x[c] == y ) :
        print('Na ', c + 1, 'ª posição encontramos o valor mínimo', y) 