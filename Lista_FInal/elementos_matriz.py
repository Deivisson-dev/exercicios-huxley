linhas_colunas = input().split()
linhas = int(linhas_colunas[0])
colunas = int(linhas_colunas[1])

matriz = []
for i in range(linhas):
    matriz.append([])
    for j in range(colunas):
        matriz[i].append(int(input()))

diagonal_principal = []
diagonal_secundaria = []
for i in range(linhas):
    for j in range(colunas):
        if i == j:
            diagonal_principal.append(matriz[i][j])
        if i + j == linhas - 1:
            diagonal_secundaria.append(matriz[i][j])

print("Matriz formada:")
for i in range(linhas):
    print(' '.join(map(str, matriz[i])))

if linhas == colunas:
    print(f"A diagonal principal e secundaria tem valor(es) {sum(diagonal_principal)} e {sum(diagonal_secundaria)} respectivamente.")
else:
    print("A diagonal principal e secundaria nao pode ser obtida.")


num_menores_que_0 = 0
for el in matriz:
    for num in el:
        if num < 0:
            num_menores_que_0 += 1

print(f"A matriz possui {num_menores_que_0} numero(s) menor(es) que zero.")

num_maiores_que_0 = 0
for el in matriz:
    for num in el:
        if num > 0:
            num_maiores_que_0 += 1

print(f"A matriz possui {num_maiores_que_0} numero(s) maior(es) que zero.")