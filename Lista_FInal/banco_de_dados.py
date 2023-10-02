qtd = int(input())

usuarios = []

for i in range(qtd):
    idade = int(input())
    nome = input()
    sexo = input()
    civil = input()
    n_amigos = int(input())
    n_fotos = int(input())
    usuarios.append({nome: [idade, sexo, civil, n_amigos, n_fotos]})

for k in usuarios:
    for key, value in k.items():
        print("Idade: " + str(value[0]))
        print(f"Nome: {key}")
        print("Sexo: " + value[1])
        print("Estado Civil: " + value[2])
        print("Numero de amigos: " + str(value[3]))
        print("Numero de fotos: " + str(value[4]))
        print()