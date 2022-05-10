# Testes com append

import random
#random.seed(8)

# Criando lista de números e de operações vazias
list_num1 , list_num2 , list_op,list_result = [], [], [], []

for i in range(10):
    num = random.randint(-10,10)
    list_num1.append(num)
    num = random.randint(-10,10)
    list_num2.append(num)
    op = random.randint(-10,10)%4

    list_op.append(op)
print(list_num1,"\n",list_num2,"\n",list_op)

for i in range(10):
    if list_op[i] == 0:
        result = list_num1[i] + list_num2[i]
        print(list_num1[i],'+',list_num2[i],'=',result)
    elif list_op[i] == 1:
        result = list_num1[i] - list_num2[i]
        print(list_num1[i],'-',list_num2[i],'=',result)
    elif list_op[i] == 2:
        result = list_num1[i] * list_num2[i]
        print(list_num1[i],'x',list_num2[i],'=',result)
    elif list_op[i] == 3:
        if list_num2[i] == 0 :
            result = "null"
            print(list_num1[i],'/',list_num2[i],'= null')
        else:
            result = list_num1[i] / list_num2[i]
            print(list_num1[i], '/', list_num2[i],'=',result)
    list_result.append(result)

print(list_result)