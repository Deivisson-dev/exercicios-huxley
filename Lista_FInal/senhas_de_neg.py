qtd_senha = int(input())

criptografia = {"0": "6", "1": "7", "2": "9", "3": "8", "4": "A", "5": "2", "6": "B", "7": "F", "8": "1", "9": "C", "A": "0", "B": "D", "C": "E", "D": "3", "E": "5", "F": "4"}

senhas_criptografadas = []

for i in range(qtd_senha):
    senha_criptografada = ""
    senhas = input()

    if not senhas.isalnum() and not senhas.isupper():
        print("Alguma senha eh invalida!")
        senhas_criptografadas = []  # Limpa a lista de senhas criptografadas
        break  # Sai do loop

    for char in senhas:
        if char in criptografia:
            senha_criptografada += str(criptografia[char])
        else:
            senha_criptografada += char  # Se o caractere não estiver no dicionário, mantenha-o inalterado
    senhas_criptografadas.append(senha_criptografada)  # Adicione a senha criptografada à lista

if senhas_criptografadas:  # Verifica se a lista de senhas criptografadas não está vazia
    for senha in senhas_criptografadas:
        print(f"-{senha}", end="")
    soma = 0
    for senha in senhas_criptografadas:
        soma += len(senha)
    print(f" {soma}")