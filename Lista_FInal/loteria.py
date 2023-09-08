pessoas = {}

while True:
    entrada = input("")
    

    if entrada == 'FIM':
        break
    
    dados = entrada.split()
    nome = dados[0]
    numeros = [int(numero) for numero in dados[1:]]
    
    pessoas[nome] = numeros

numeros_sorteados = input("")
numeros_sorteados_form = numeros_sorteados.split("-")
numeros_sorteados = [int(numero) for numero in numeros_sorteados_form]


acertos_por_pessoa = []

for nome, numeros in pessoas.items():
    num_acertos = 0
    for numero in numeros:
        if numero in numeros_sorteados:
            num_acertos += 1
    tupla = (nome, num_acertos)
    acertos_por_pessoa.append(tupla)


acertos_por_pessoa = sorted(acertos_por_pessoa, key=lambda x: (x[1], x[0]))


for nome, num_acertos in acertos_por_pessoa:
    print(f"{nome} {'+' * num_acertos}")