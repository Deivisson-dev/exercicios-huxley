qtd = int(input())

presentes = {}


for i in range(qtd):
    nome_presente = input().split()
    presentes[nome_presente[0]] = nome_presente[1:]

while True:
    nome_presentes = input().split()
    if nome_presentes[0] == "FIM":
        break
    for nome, presente in presentes.items():
        if nome_presentes[0] == nome:
            if nome_presentes[1] in presente:
                print("Uhul! Seu amigo secreto vai adorar")
            else:
                print("Tente Novamente!")