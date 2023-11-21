ph = float(input("digite quanto voce recebe por hora: "))
ht = float(input("quantas horas voce trabalhou esse mês: "))
sb = ph * ht
if sb <= 900:
    desconto_ir = 0
elif sb <=1500:
    desconto_ir = 5
elif sb <=2500:
    desconto_ir = 10
else:
    desconto_ir=20

ir=sb*(desconto_ir/100)
inss=sb*(10/100)
fgts=sb*(11/100)
desconto=ir +inss
sl=sb -desconto
print("salario bruto R$",sb)
print("IR (5%) R$",ir)
print("INSS (10%) R$",inss)
print("FGTS (11%) R$", fgts)
print("total de descontos R$", desconto)
print("salario liquido R$", sl)