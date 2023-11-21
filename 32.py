n1 =float(input("nota parcial-1: "))
n2 =float(input("nota parcial-2: "))
n3=(n1+n2)/2
if n3 >=9:
   a = "A"
elif n3>=7.5:
    a = "B"
elif n3>=6:
    a = "C"
elif n3>=4:
    a = "D"
else:
    a = "E"

if a == "D" or a == "E":
    print("reprovado")
else:
    print("aprovado")