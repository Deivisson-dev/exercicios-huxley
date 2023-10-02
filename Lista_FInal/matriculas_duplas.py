programacao_ii = list(map(int, input().split()))
programacao_iii = list(map(int, input().split()))
set_programacao_ii = set(programacao_ii)


alunos_em_ambas_disciplinas = []

for matricula in programacao_iii:
    if matricula in set_programacao_ii:
        alunos_em_ambas_disciplinas.append(matricula)

for matricula in programacao_ii:
    if matricula in alunos_em_ambas_disciplinas:
        print(matricula, end=' ')

print()