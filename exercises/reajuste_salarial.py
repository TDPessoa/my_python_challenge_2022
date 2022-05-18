"""Comentário Original:
        As Organizações Tabajara resolveram dar um aumento de salário \
        aos seus colaboradores e lhe contrataram para desenvolver o \
        programa que calculará os reajustes. Elaborar um algoritmo que \
        leia o salário de um colaborador e façao reajuste segundo o \
        seguinte critério, baseando-se no salário atual.

            até R$280 (inclusive)                                  20%
            entre R$280,00 e R$700,00 (inclusive)                  15%
            entre R$700,00 e R$1500 (inclusive)                    10%
            acima de R$1500,00                                      5%

    Após o aumento ser realizado, deve-se imprimir na tela:
        • o	salário	antes do reajuste (em R$);
        • o	percentual de aumento aplicado (em %);
        • o	valor do aumento (em R$);
        • o	novo salário, após o aumento (em R$).

Comentário Recente:
    Este foi um exercício da faculdade, só para demonstrar as \
    operadorações de inequação e multiplicação do python."""

# Entrada do dado
base = float(input('Bem vindo. Digite seu salário para que eu possa calcular '
                   + 'o reajuste:'))

# Manipulação do dado
if 0 < base <= 280:
    correcao = base * 0.2
    porcentagem = 20

elif 280 < base <= 700:
    correcao = base * 0.15
    porcentagem = 15

elif 700 < base <= 1500:
    correcao = base * 0.1
    porcentagem = 10

elif base > 1500:
    correcao = base * 0.05
    porcentagem = 5

else:
    print('Valor não aceito.')

# Saida de dados
print('------------------------------')
print(f'Seu salário de R${base} recebeu reajuste de {porcentagem}%.')
print(f'Com um aumento no valor de R${correcao}, seu salário agora é de'
      + f'R${base + correcao}.')
