matricula_menor_cre = 0
menor_cre = 0
soma = 0
tot = 0
while True:
    matricula = input()
    if matricula == "999":
        break
    cre = float(input())
    tot += 1
    soma += cre
    if menor_cre == 0:
        menor_cre = cre
        matricula_menor_cre = matricula
    if cre < menor_cre:
        menor_cre = cre
        matricula_menor_cre = matricula

media = soma / tot
print(matricula_menor_cre)
print(f"{media:.2f}")