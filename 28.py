turno = input("Em que turno você estuda?, (M-matutino, V-vespertino, N-noturno): ")
if turno == "m" or turno == "M":
    print("Bom dia")
elif turno == "v" or turno == "V":
    print("Boa tarde")
elif turno == "n" or turno == "N":
    print("Boa noite")
else:
    print("INVALIDO")