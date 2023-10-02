dimensoes_da_matriz = input().split()
colunas = int(dimensoes_da_matriz[0])
linhas = int(dimensoes_da_matriz[1])
matriz = []
for i in range(colunas):
    linha = input().split()
    matriz.append(linha)
print("Digite as dimensoes da matriz:")
print("Digite os elementos da matriz:")
print("Matriz transposta:")


for i in range(linhas):
    for j in range(colunas):
        print(f"{matriz[j][i]:5}", end=" ")
    print()