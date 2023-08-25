competidores = int(input())
pontos_minimos = int(input())
tot_convocados = 0
for i in range(competidores):
    primeira_fase = int(input())
    segunda_fase = int(input())
    if (primeira_fase == 0) or (segunda_fase == 0):
        continue
    if (primeira_fase + segunda_fase) >= pontos_minimos:
        tot_convocados += 1
print(tot_convocados)