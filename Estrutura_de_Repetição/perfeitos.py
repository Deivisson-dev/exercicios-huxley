n = int(input())
soma = 0
tot_perf = 0
divisores = []
perfeitos = []
for i in range(1, n):
    for j in range(1, i):
        if i % j == 0:
            divisores.append(j)
    for k in divisores:
        soma += k
    if soma == i:
        perfeitos.append(i)
    divisores = []
    soma = 0
for elemento in perfeitos:
    print(elemento)