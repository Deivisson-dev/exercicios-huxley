tot_aprovado = 0
while True:
    qtd_questoes_portugues = int(input())
    if qtd_questoes_portugues < 0:
        break
    qtd_questoes_matematica = int(input())
    nota_redaçao = float(input())
    if (qtd_questoes_portugues >= 40) and (qtd_questoes_matematica >= 21) and (nota_redaçao >= 7):
        tot_aprovado += 1
print(tot_aprovado)