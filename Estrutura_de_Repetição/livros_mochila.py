soma = 0
livros = 0
while True:
    peso = int(input())
    soma += peso
    if soma > 18:
        break
    livros += 1
print(livros)