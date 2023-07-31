ano = 0
dia_maximo = 0
dia = int(input())
# Verifica se o dia está no intervalo correto para os meses com 31 dias

while True:
    if dia < 1 or dia > 31:
        print("Dia inexistente")
        break
    else:
        mes = int(input())
        
        # Verifica se o mês está no intervalo correto
        if mes < 1 or mes > 12:
            print("Mês inexistente")
            break
        else:
            # Verifica os meses com 31 dias
            if mes in [1, 3, 5, 7, 8, 10, 12]:
                if dia < 1 or dia > 31:
                    print("Esse dia não existe nesse mês")
                    break
                else:
                    ano = int(input())
                    # Verifica se o ano está no intervalo permitido
                    if ano < 1900 or ano > 2020:
                        print("Ano inexistente")
                        break
                    else:
                        print("Data Validada")
            # Verifica os meses com 30 dias
            elif mes in [4, 6, 9, 11]:
                if dia < 1 or dia > 30:
                    print("Esse dia não existe nesse mês")
                    break
                else:
                    ano = int(input())
                    # Verifica se o ano está no intervalo permitido
                    if ano < 1900 or ano > 2020:
                        print("Ano inexistente")
                        break
                    else:
                        print("Data Validada")
                        break
            # Verifica o mês de fevereiro
            elif mes == 2:
                if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): 
                    dia_maximo = 29
                else:
                    dia_maximo = 28
                    if dia == 29:
                        print("Esse ano não é bissexto")
                        break
                            
                if dia >= 1 and dia <= dia_maximo:
                    ano = int(input())
                    if ano < 1900 or ano > 2020:
                        print("Ano inexistente")
                        break
                else:
                    print("Esse dia não existe nesse mês")
                    break