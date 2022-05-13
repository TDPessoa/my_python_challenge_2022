'''
Comentário Recente:
    Este script foi elaborado para testar se o infinito imaginário    \
    das casas decimais dos números reais se aplica à lógica da        \
    programação.
    
    Aos que desconhecem, a Corrida de Aquilles seria um paradoxo onde \
    o próprio correria com uma tartaruga, a qual teria uma vantagem   \
    e sairia na frente de aquiles, que deveria parar sempre no ponto  \
    em que a tartaruga chegou com dada vantagem, porém a tartaruga se \
    manteria em movimento, tendo assim, uma nova distancia de vantagem.

    Se é concluido que Aquiles nunca terminaria tal corrida, pois     \
    uma vez que ele sempre tem que parar no ponto em que a tartaruga  \
    alcançou e a mesma está na frente, ele sempre terá(mesmo que seja \
    uma fração) algo a mais para se percorrer.

    Então o script se fundamenta em um limite, e a tartaruga sempre   \
    irá percorrer metade do que falta para a linha de chegada, daí 1  \
    na primeira, 1/2 na segunda, 1/4 na terceira... ou melhor, sempre 
    multiplicando por 2 o divisor do valor a ser adicionado a conta. 
    A cada vez que Aquilles para, é adicionado 1 a "paradas".

'''

# Declarando variáveis
passo_aquilles, passo_tartaruga, paradas = 0, 1, 0

# Laço de repetição
while (passo_aquilles < 2):
    passo_aquilles += 1 / passo_tartaruga
    passo_tartaruga *= 2
    paradas += 1

# Impressão de informações relevantes
print('Quantidade de paradas =', paradas )
print('Valor final do divisor =', passo_tartaruga)