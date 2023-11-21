a=float (input('digite o valor de a: '))
if a ==0:
    print('não e uma equação do segundo grau')
else:
    b =float(input('digite o valor de b: '))
    c = float(input('digite o  valor de c: '))
    delta=(b**2) - (4 *a*c)
    if delta<0:
        print('delta menor que zero, não a raizes reais')
    elif delta==0:
        r=(-b)/(2*a)
        print('delta é zero, a raiz é',r)
    else:
        r1= (-b-(delta**(1/2)))/(2*a)
        r2=(-b-(delta**(1/2)))/(2*a)
        print("delta  maior que zero, a raiz 1 é",r1,',a raiz 2 é',r2)