pr1=float(input('digite o preço de um produto: '))
pr2=float(input('digite o preço do segundo produto: '))
pr3=float(input('digite o preço de outro produto: '))
if pr1<pr2 and pr3:
    print('compre esse produto de {}'.format(pr1))
elif pr2<pr1 and pr3:
    print('compre esse produto de {}'.format(pr2))
else:
    print('compre o produto que custa {}'.format(pr3))