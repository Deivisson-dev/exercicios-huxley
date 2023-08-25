valor_por_caixa = 7.89
pregos_por_caixa = 12
pregos_necessarios = []
    
while True:
    qtd_pregos = int(input())
    if qtd_pregos % 2 == 1:
        break  # Encerra o loop se for digitado um número ímpar
    pregos_necessarios.append(qtd_pregos)



total_pregos = sum(pregos_necessarios)
total_caixas = (total_pregos + pregos_por_caixa - 1) // pregos_por_caixa
total_gasto = total_caixas * valor_por_caixa
pregos_sobrando = (total_caixas * pregos_por_caixa) - total_pregos


print(f"{total_gasto:.2f}")
print(f"{pregos_sobrando}")