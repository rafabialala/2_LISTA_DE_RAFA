morango = float(input("Digite quantos quilos de morango foram comprados: "))
maca = float(input("Digite quantos quilos de maçã foram comprados: "))
valor = 0

if morango <= 5:
    valor += morango * 2.5
else:
    valor += morango * 2.2
if maca <= 5:
    valor += maca * 1.8
else:
    valor += maca * 1.5

if (morango + maca) > 8 or valor > 25:
    valor -= valor * 10 / 100

print("O valor a ser pago é R$ {}".format(valor))