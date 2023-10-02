def multiplicar_matrizes(A, B):
    linhas_A, colunas_A = len(A), len(A[0])
    linhas_B, colunas_B = len(B), len(B[0])

    if colunas_A != linhas_B:
        return None

    C = [[0 for _ in range(colunas_B)] for _ in range(linhas_A)]

    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(colunas_A):
                C[i][j] += A[i][k] * B[k][j]

    return C

N, M, O = map(int, input().split())

A = []
for _ in range(N):
    linha = list(map(int, input().split()))
    A.append(linha)

B = []
for _ in range(M):
    linha = list(map(int, input().split()))
    B.append(linha)

resultado = multiplicar_matrizes(A, B)

for linha in resultado:
    print(" ".join(map(str, linha)))
