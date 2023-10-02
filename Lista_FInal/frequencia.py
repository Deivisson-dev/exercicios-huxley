n = int(input())

alunos = set()

for i in range(n):
    matricula = int(input())
    alunos.add(matricula)

print(len(alunos))