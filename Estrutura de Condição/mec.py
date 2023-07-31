qtd_livros = int(input())
qtd_alunos = int(input())

qtd_livros_por_aluno = qtd_alunos / qtd_livros

if qtd_livros_por_aluno <= 8:
    print("A")
elif qtd_livros_por_aluno >= 9 and qtd_livros_por_aluno <= 12:
    print("B")
elif qtd_livros_por_aluno >= 13 and qtd_livros_por_aluno <= 18:
    print("C")
elif qtd_livros_por_aluno > 18:
    print("D")