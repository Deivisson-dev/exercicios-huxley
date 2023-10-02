linha = int(input())
operação = input()
matriz = []
for i in range(1,13):
    matr = input().split()
    matriz.append([int(x) for x in matr])

for k in matriz[linha]:
    if operação == "S":
        soma = sum(matriz[linha])
        print(f"{soma:.1f}")
        break
    elif operação == "M":
        media = sum(matriz[linha])/12
        print(f"{media:.1f}")
        break