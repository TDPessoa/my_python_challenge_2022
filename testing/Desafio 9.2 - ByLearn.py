'''

Desafio ByLearn-- Calculadora

Classe calculadora que contém os seguintes metodos:
	- Somar
	- Subtrair
	- Multiplicar
	- Dividir

Ps: Os métodos devém funcionar com dois números.
Ps2: Todos os métodos retornam o valor.

A classe também contém as propriedades(atributos):
	primeiro_valor
	segundo_valor

Ps3: Os valores são passados por parâmetro.
Ps4: Os valores serão passados pelo usuário(input).

'''

class Calculadora(object):
	def soma(self, primeiro_valor, segundo_valor):
		return primeiro_valor + segundo_valor
	def subtr(self, primeiro_valor, segundo_valor):
		return print( primeiro_valor - segundo_valor)
	def multi(self, primeiro_valor, segundo_valor):
		return primeiro_valor * segundo_valor
	def divis(self, primeiro_valor, segundo_valor):
		return primeiro_valor / segundo_valor

calc = Calculadora()

print(calc.divis(640, 2))
print(calc.multi(7, 9))
print(calc.soma(444, 666))
print(calc.subtr(114, 44))