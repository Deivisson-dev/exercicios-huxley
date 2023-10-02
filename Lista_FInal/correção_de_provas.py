from collections import Counter

gabarito = input()
lista_de_caracteres = list(gabarito)

alunos = {}

while True:
    entrada = input()
    if entrada == '9999':
        break
    else:
        partes = entrada.split()
        numero_aluno = partes[0]
        respostas_aluno = list(partes[1])
        alunos[numero_aluno] = respostas_aluno

for numero, respostas in alunos.items():
    nota_final = sum([1 for i in range(len(respostas)) if respostas[i] == lista_de_caracteres[i]])
    alunos[numero].append(nota_final)

for numero, notas in alunos.items():
    print(f'{numero} {notas[-1]:.1f}')

numero_de_alunos = len(alunos)
numero_aprovados = sum(1 for numero, notas in alunos.items() if notas[-1] >= 6)
taxa_aprovacao = numero_aprovados / numero_de_alunos * 100
taxa_aprovacao = round(taxa_aprovacao, 1)
print(f'{taxa_aprovacao:.1f}%')

# Encontrar a nota com a maior frequência absoluta
todas_as_notas = []
for numero, notas in alunos.items():
    nota_final = notas[-1]
    todas_as_notas.append(nota_final)

frequencia_notas = {}

# Conta a frequência de cada nota
for nota in todas_as_notas:
    if nota in frequencia_notas:
        frequencia_notas[nota] += 1
    else:
        frequencia_notas[nota] = 1

# Encontrar a nota com a maior frequência
mais_se_repete = None
max_frequencia = 0

for nota, frequencia in frequencia_notas.items():
    if frequencia > max_frequencia:
        max_frequencia = frequencia
        mais_se_repete = nota


print(f'{mais_se_repete:.1f}')