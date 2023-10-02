n = int(input())
matriz = []
for _ in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)


soma_linha = sum(matriz[0])
is_quadrado_magico = True
for linha in matriz:
    if sum(linha) != soma_linha:
        is_quadrado_magico = False
        break


for coluna in range(n):
    soma_coluna = 0
    for linha in matriz:
        soma_coluna += linha[coluna]
    if soma_coluna != soma_linha:
        is_quadrado_magico = False
        break


soma_diagonal_principal = 0
soma_diagonal_secundaria = 0
for i in range(n):
    soma_diagonal_principal += matriz[i][i]
    soma_diagonal_secundaria += matriz[i][n - i - 1]

if (soma_diagonal_principal != soma_linha) or (soma_diagonal_secundaria != soma_linha):
    is_quadrado_magico = False

if is_quadrado_magico:
    print(soma_linha)
else:
    print(-1)
