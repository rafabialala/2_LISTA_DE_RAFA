for numero in [
    326,
    300,
    100,
    320,
    310,
    305,
    301,
    101,
    311,
    111,
    25,
    20,
    10,
    21,
    11,
    1,
    7,
    16,
]:
   
    print(f"\nNumero: {numero}")
    unidade = numero % 10
    dezena = (numero % 100) // 10
    centena = numero // 100
    separador1 = ""
    separador2 = ""
   
    if centena > 0 and dezena > 0 and unidade > 0:
        separador1 = " , " 
      
        separador2 = " e " 
   
    elif centena > 0 and dezena > 0:
        separador1 = " e " 
        separador2 = ""
   
    elif (centena > 0 and unidade > 0) or (dezena > 0 and unidade > 0):
        separador1 = ""  
        separador2 = " e " 
   
    if centena > 0:
        if centena == 1:
           
            centena = "1 centena"
        else:
         
            centena = f"{centena} centenas"
    else:
        centena = "" 
    if dezena > 0:
        if dezena == 1:
            dezena = "1 dezena"
        else:
            dezena = f"{dezena} dezenas"
    else:
        dezena = ""
   
    if unidade > 0:
        if unidade == 1:
            unidade = "1 unidade"
        else:
            unidade = f"{unidade} unidades"
    else:
        unidade = ""

    
    print(f"{centena}{separador1}{dezena}{separador2}{unidade}")