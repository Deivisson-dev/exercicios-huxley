dia = int(input())
bissexto = True
if dia < 1 or dia > 31:
    print("Dia inexistente")
else:
    mes = int(input())

    # Verifica se o mês está no intervalo correto
    if mes < 1 or mes > 12:
        print("Mês inexistente")
    else:
        # Verifica os meses com 31 dias
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            if dia < 1 or dia > 31:
                print("Esse dia não existe nesse mês")
            else:
                ano = int(input())
                # Verifica se o ano está no intervalo permitido
                if ano < 1900 or ano > 2020:
                    print("Ano inexistente")
                else:
                    print("Data Validada")
                    data_validada = True
        # Verifica os meses com 30 dias
        elif mes in [4, 6, 9, 11]:
            if dia > 30:
                print("Esse dia não existe nesse mês")
            else:
                ano = int(input())
                # Verifica se o ano está no intervalo permitido
                if ano < 1900 or ano > 2020:
                    print("Ano inexistente")
                else:
                    print("Data Validada")
                    data_validada = True
        # Verifica o mês de fevereiro
        elif dia > 29 and mes == 2 and bissexto == True:
            print("Esse dia não existe nesse mês")

        elif mes == 2:
            ano = int(input())
            if ano < 1900 or ano > 2020:
                print("Ano inexistente")
            else:
                bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
                dia_maximo = 29 if bissexto else 28
                if dia > dia_maximo:
                    print("Esse ano não é bissexto")
                else:
                    print("Data Validada")
                    data_validada = True

if data_validada:
    lista_datas = [dia, mes, ano]
    print(lista_datas)