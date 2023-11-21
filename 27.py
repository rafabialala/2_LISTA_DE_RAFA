n1=int(input('digite um numero: '))
n2=int(input('digite o segundo numero: '))
n3=int(input('digite o terceiro numero: '))
if n1>n2>n3:
    print('a sequencia é {},{},{}'.format(n1,n2,n3))
elif n2>n3>n1:
    print('a sequencia é {},{},{}'.format(n2,n3,n1))
elif n3>n2>n1:
    print('a sequencia é {},{},{}'.format(n3,n2,n1))
elif n1>n3>n2:
    print('a sequencia é {},{}`,{}'.format(n1,n3,n2))
elif n3>n1>n2:
    print('a sequencia é {},{},{}'.format (n3,n1,n2))
else:
    print('a sequencia é {},{},{}'.format (n2,n1,n3))