dias = int(input())
quilometragem_total = int(input())

valor_diaria = 90
cota_km_diaria = 100
taxa_excesso_km = 12


valor_total = 0
if quilometragem_total <= cota_km_diaria * dias:
    valor_total = valor_diaria * dias
else:
    km_excesso = quilometragem_total - (cota_km_diaria * dias)
    valor_total = (valor_diaria * dias) + (km_excesso * taxa_excesso_km)

print("{:.2f}".format(valor_total))