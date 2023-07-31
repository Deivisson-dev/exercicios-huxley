idade =  int(input())
nota1 = float(input())
nota2 = float(input())
nota_reposicao = float(input())

if nota1 >= nota2 and nota1 >= nota_reposicao:
    maior1 = nota1
    if nota2 >= nota_reposicao:
        maior2 = nota2
    else:
        maior2 = nota_reposicao
elif nota2 >= nota1 and nota2 >= nota_reposicao:
    maior1 = nota2
    if nota1 >= nota_reposicao:
        maior2 = nota1
    else:
        maior2 = nota_reposicao
else:
    maior1 = nota_reposicao
    if nota1 >= nota2:
        maior2 = nota1
    else:
        maior2 = nota2




if idade >= 18:
    media = (nota1 + nota2) / 2
    media_final = (nota1 * 6 + nota2 * 6 + nota_reposicao * 3) / 15
else:
    if nota1 < 7 or nota2 < 7:
        media_final = (maior1 + maior2) / 2
    else:
        media_final = (nota1 + nota2) / 2





if media_final >= 5.5 and (nota1 >= 4.0 and nota2 >= 4.0 and nota_reposicao >= 4.0):
    print("Aprovado")
else:
    print("Reprovado")