total_a = []
total_b = []
total_c = []
total_brancos = []
total_nulos = []
while True:
    seccao = int(input())
    if seccao == 0:
        break
    voto_a = int(input())
    total_a.append(voto_a)
    voto_b = int(input())
    total_b.append(voto_b)
    voto_c = int(input())
    total_c.append(voto_c)
    votos_brancos = int(input())
    total_brancos.append(votos_brancos)
    votos_nulos = int(input())
    total_nulos.append(votos_nulos)
    total_votos = [sum(total_a), sum(total_b), sum(total_c), sum(total_brancos), sum(total_nulos)]

print(f"Numeros de votantes = {sum(total_votos)}")
print(f'Votos candidato A: {total_votos[0]}')
print(f'Votos candidato B: {total_votos[1]}')
print(f'Votos candidato C: {total_votos[2]}')
print(f'Votos em branco: {total_votos[3]}')
print(f'Votos nulos: {total_votos[4]}')
