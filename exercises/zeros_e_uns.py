'''Comentário Original:
    Elaborar um algoritmo que leia 12 números binários, isto é, \
    somente serão permitidos números “0s” ou “1s” (deve-se fazer a \
    proteção de dados). Calcule e imprima:

        • A quantidade de números “1s” e números “0s”. Deve-se também \
        comparar os resultados para saber se existem mais “1s” ou “0s”\
        ou se as quantidades são iguais (deve-se imprimir uma mensagem \
        ao usuário);
        • O percentual de números “0s” e “1s” digitados.
Comentário Recente:
    Outro exercício da faculdade.'''

zeros , uns = 0 , 0

print('Bem vindo ao contador binário.')
for c in range (0, 12):
    while True:
        num = int(input('Entre com zeros ou uns:'))
        if num == 0 or num == 1:
            break

        else:
            print('Inválido')

    if num == 1:
        uns += 1

    else:
        zeros += 1


porcent_zeros = (zeros / 12) * 100
porcent_uns = (uns / 12) * 100

print('Foram inseridos {} zeros e {} uns.'.format(zeros, uns))
print('A porcentagem de zeros é de {:.1f}% e de uns é de {:.1f}%.'.format(porcent_zeros, porcent_uns))
