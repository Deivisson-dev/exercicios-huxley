total_a = []
total_b = []
total_c = []
total_brancos = []
total_nulos = []
validos = []
total_votos = [0,0,0,0,0]
while True:
        seccao = int(input())
        if seccao == 0:
            break
        voto_a = int(input())
        validos.append(voto_a)
        total_a.append(voto_a)
        voto_b = int(input())
        validos.append(voto_b)
        total_b.append(voto_b)
        voto_c = int(input())
        validos.append(voto_c)
        total_c.append(voto_c)
        votos_brancos = int(input())
        total_brancos.append(votos_brancos)
        votos_nulos = int(input())
        total_nulos.append(votos_nulos)
        total_votos = [sum(total_a), sum(total_b), sum(total_c), sum(total_brancos), sum(total_nulos)]


print(f"Numero de votantes: {sum(total_votos)}")
print(f'Total A: {total_votos[0]}')
print(f'Total B: {total_votos[1]}')
print(f'Total C: {total_votos[2]}')
print(f'Brancos: {total_votos[3]}')
print(f'Nulos: {total_votos[4]}')
print(f"Validos: {sum(validos)}")


if (sum(total_a) > sum(total_b)) and (sum(total_a) > sum(total_c)):
        print("Candidato mais votado: A")
        campeao_a = True
        campeao_b = False
        campeao_c = False
elif (sum(total_b) > sum(total_a)) and (sum(total_b) > sum(total_c)):
        print("Candidato mais votado: B")
        campeao_b = True
        campeao_a = False
        campeao_c = False
elif (sum(total_c) > sum(total_a)) and (sum(total_c) > sum(total_b)):
        print("Candidato mais votado: C")
        campeao_c = True
        campeao_a = False
        campeao_b = False
else:
        print("Candidato mais votado: ")
        campeao_a = False
        campeao_b = False
        campeao_c = False

if (sum(total_nulos) + sum(total_brancos)) < (sum(total_a) + sum(total_b) + sum(total_c)):
        print(f"Eleicao valida? {True}")
else:
        print(f"Eleicao valida? {False}")

metade = sum(validos) / 2


if total_votos == [0,0,0,0,0]:
    print(f"Segundo turno? {False}")
elif campeao_a == True:
    if (sum(total_a) > metade):
              print(f"Segundo turno? {False}")
    elif (sum(total_a) == metade):
              print(f"Segundo turno? {False}")
    elif (sum(total_a) < metade):
            print(f"Segundo turno? {True}")
elif campeao_b == True:
    if sum(total_b) > metade:
        print(f"Segundo turno? {False}")
    elif sum(total_b) == metade:
        print(f"Segundo turno? {False}")
    elif sum(total_b) < metade:
        print(f"Segundo turno? {True}")
elif campeao_c  == True:
    if sum(total_c) > metade:
        print(f"Segundo turno? {False}")
    elif sum(total_c) == metade:
        print(f"Segundo turno? {False}")
    elif sum(total_c) < metade:
        print(f"Segundo turno? {True}")
elif campeao_a == False and campeao_b == False and campeao_c == False:
    print(f"Segundo turno? {True}")