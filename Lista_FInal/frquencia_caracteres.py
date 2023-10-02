# Receber o texto em uma única linha
texto = input()

caracteres = list(texto)
caracteres_unicos = []

for caractere in caracteres:
    if caractere not in caracteres_unicos:
        caracteres_unicos.append(caractere)


caracteres_unicos.sort(reverse=True)
for caractere in caracteres_unicos:
    count = caracteres.count(caractere)
    print(f"{caractere} {count}")
