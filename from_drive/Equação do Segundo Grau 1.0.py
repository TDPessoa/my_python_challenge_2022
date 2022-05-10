import math
n1= int (input("Valor de a"))
n2= int (input("Valor de b"))
n3= int (input("Valor de c"))
D= ((n2**2)-(4*n1*n3))
RD=math.sqrt(D)
X1= (-(n2)+RD)
X2= (-(n2)-RD)
print ("O Valor de X1 é {} e o valor de X2 é {}" .format(X1/(n1*2), X2/(n1*2)))