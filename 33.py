l1 = float(input("digite o valor de primeiro dos lados do triãngulo: "))
l2 = float(input("digite o valor de segundo dos lados do triãngulo: "))
l3 = float(input("digite o valor de terceiro dos lados do triãngulo: "))

if ((l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1)):
    if l1 == l2 and l2 == l3:
        print("É um triângulo equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("É um triângulo isoceles")
    else:
        print('escaleno')