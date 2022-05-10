print("Reajuste de salário Tabajara.")
x=float(input("Qual é o valor do salário atual?"))
if x<=280:
    p="20%."
    y=x*0.2
    z=x+y
elif x>280 and x<=700:
    p="15%."
    y=x*0.15
    z=x+y
elif x>700 and x<=1500:
    p="10%."
    y=x*0.1
    z=x+y
else:
    p="5%."
    y=x*.05
    z=x+y
print("O salário antes do reajuste:R$",x)
print("Foi aumentado em",p)
print("O valor do aumento foi de: R$",y)
print("O salário após o aumento é:",z)