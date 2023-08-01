alunos = int(input())
preco_unidade = 2.20
conj_tres = alunos // 3
resto = alunos % 3
valor_total = (conj_tres * 2 + resto) * preco_unidade
print(f'{valor_total:.2f}')