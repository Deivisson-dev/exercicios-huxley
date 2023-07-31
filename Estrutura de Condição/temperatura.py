temperatura = float(input())
sintomas = input()

if sintomas != "S" and sintomas != "N":
    print("Erro")
elif (temperatura >= 37) and (sintomas == "S"):
    print("Exames Especiais")
elif (temperatura >= 37) and (sintomas == "N"):
    print("Exames Basicos")
elif (temperatura < 37) and (sintomas == "N"):
    print("Liberado")
elif (temperatura < 37) and (sintomas == "S"):
    print("Exames Basicos")
