y = int(input())
tot_y = 0
tot_valores = 0
soma = 0
total_menor_0 = 0
valores = []
intervalo = [15, 16, 17, 18, 19, 20]
media = 0
while True:
    for i in range(1, 21):
        n = int(input())
        valores.append(n)
        if n == -1:
            break
        if n == y:
            tot_y += 1
        if n not in intervalo and n > 0:
            tot_valores += 1
            soma += n
            media = soma / tot_valores
    break
print(f"O número {y} apareceu {tot_y} vez(es)")
for elemento in valores:
    if elemento < 0:
        total_menor_0 += 1


if total_menor_0 == tot_valores:
    print(f"Sem valores para calcular a média")
elif tot_valores == 0:
    print(f"Sem valores para calcular a média")
else:
    print(f"A média dos valores é {media:.2f}")