data = input('digite uma data no formato da dd/mm/aaaa: ')
dia,mes,ano=data.split('/')
dia,mes,ano =int(dia), int(mes), int(ano)
if ano < 0:
    print('ano invalido!')
else:
    if mes<1 or mes >12:
        print('mes invalido!')
    elif mes in[1,3,5,7,8,10,12]:
        if dia > 0 and dia < 31:
            print('data valida')
        else:
            print('dia invalido')
    elif mes in [4,6,9,11]:
        if dia > 0 and dia < 31:
            print('data valida')
        else:
            print('dia invalido')
    else:
        if ano % 4 == 0:
            if dia > 0 and dia < 30:
                print('data valida')
            else:
                print('dia invalido')
        else:
            if dia > 0 and dia < 29:
                print('data valida')
            else:
                print('dia invalido')