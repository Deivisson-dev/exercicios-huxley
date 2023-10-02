x = int(input())

inimigos = []

for i in range(x):
    nome = input()
    Id = input()
    level = input()
    vida = input()
    ataques = input()
    defesa = input()
    inimigos.append({nome: [Id, level, vida, ataques, defesa]})

for k in inimigos:
    for key, value in k.items():
        print(f"Nome: {key}")
        print("ID: " + value[0])
        print("Level: " + value[1])
        print("Vida: " + value[2])
        print("Ataque: " + value[3])
        print("Defesa: " + value[4])