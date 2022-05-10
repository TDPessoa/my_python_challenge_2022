'''

    As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para
desenvolver o programa que calculará os reajustes. Elaborar um algoritmo que leia o salário de um colaborador e faça
o reajuste segundo o seguinte critério, baseando-se no salário atual.

        até R$280 (inclusive)                                  20%
        entre R$280,00 e R$700,00 (inclusive)                  15%
        entre R$700,00 e R$1500 (inclusive)                    10%
        acima de R$1500,00                                      5%

Após o aumento ser realizado, deve-se imprimir na tela:
    • o	salário	antes do reajuste (em R$);
    • o	percentual de aumento aplicado (em %);
    • o	valor do aumento (em R$);
    • o	novo salário, após o aumento (em R$).
'''

x=int(input('Bem vindo. Digite seu salário para que eu possa calcular o reajuste:'))

if x>0 and x<=280:
    y=x*0.2
    z=20
elif x>280 and x<=700:
    y=x*0.15
    z=15
elif x>700 and x<=1500:
    y=x*0.1
    z=10
elif x>1500:
    y=x*0.05
    z=5
else:
    print("Valor não aceito.")

print('------------------------------')
print('Seu salário de R$',x,'recebeu reajuste de',z,'%.')
print('Com um aumento no valor de R$',y,', seu salário agora é de R$',x+y,'.')
