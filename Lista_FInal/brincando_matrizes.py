matriz = []

for i in range(9):
    elementos = int(input())
    matriz.append(elementos)

media = sum(matriz) / 9
maior = max(matriz)
menor = min(matriz)
if maior > 0:
    delta = 1
elif maior < 0:
    delta = -1
else:
    delta = 0

soma_diag = matriz[0] + matriz[4] + matriz[8]
print(f"{media:.2f} {maior} {delta} {soma_diag}")