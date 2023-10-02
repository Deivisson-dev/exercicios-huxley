n_livros = int(input())
livros = []
for i in range(n_livros):
    nome_livro = input()
    livros.append(nome_livro)

livro_referencia = input()
if livro_referencia in livros:
    print("Sim")
else:
    print("Não")