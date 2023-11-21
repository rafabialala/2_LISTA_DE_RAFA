t = float(input("digite o primeiro numero: "))
n = float(input("digite o segundo numero: "))
s = float(input("digite o terceiro numero: "))
if t > n and t > s:
    print('{}  o maior numero é.'.format(t))
elif n > t and t > s:
    print("{}  o maior numero é.".format(n))
else:
    print("{}  o maior numero é.".format(s))