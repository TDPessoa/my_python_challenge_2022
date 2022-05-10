'''
Teste de estresse com multiplas células de uma matriz.
'''

# Imports:
import random , time

# Variable <s|tart|_time> storing epoch
s_time = time.time()

# Variables for: <size> of the matriz, <min> and <max> range of integers and repetitions done.
size , min , max , work = 1024 , -1000 , 1000 , 0

# Variable starting the empty list that will be the matrix
matrix = []

# Building the matrix
for i in range ( size ) :

    line = []

    for j in range ( size ) :

        num = random.randint ( min , max )
        line.append ( num )
        work += 1

    matrix.append ( line )

# Variable for the sum of every cell in the matrix
sum = 0

# Summing every cell
for i in range ( size ) :

    for j in range ( size ) :

        sum += matrix[ i ][ j ]
        work += 1

print ( sum )

e_time = time.time() - s_time

print ( 'elapsed_time = ' , e_time , ', works_done = ' ,  work )
print ( 'works_per_sec = ' , work/e_time , ', seconds_per_work = ' , e_time/work )
