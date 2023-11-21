n1 = float(input("digite uma nota"))
n2 = float(input("digite a segunda nota: "))
total = (n1 + n2) / 2
if total ==10:
    print("voce foi Aprovado com Distinção")
elif total >= 7:
    print("voce foi aprovado")
else:
    print("voce foi Reprovado")