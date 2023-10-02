# Número de instâncias
n = int(input())

for instancia in range(1, n + 1):
    matriz = []
    for _ in range(9):
        linha = list(map(int, input().split()))
        matriz.append(linha)

    valido = True

    # Verificar linhas e colunas
    for i in range(9):
        linha = matriz[i]
        coluna = [matriz[j][i] for j in range(9)]
        if len(set(linha)) != 9 or len(set(coluna)) != 9:
            valido = False
            break

    # Verificar regiões
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            regiao = []
            for x in range(i, i+3):
                for y in range(j, j+3):
                    regiao.append(matriz[x][y])
            if len(set(regiao)) != 9:
                valido = False
                break

    resultado = "SIM" if valido else "NAO"
    
    # Imprimir resultado da instância
    print(f"Instancia {instancia}")
    print(resultado)
    print()  # Linha em branco entre as instâncias
