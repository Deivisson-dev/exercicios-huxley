salario = float(input())

salario_bonus = salario * 1.75
bonus_final = salario_bonus - salario

if bonus_final < 2000:
    print("ARGENTINA")
elif bonus_final >= 2000 and bonus_final <= 3000:
    print("ESPANHA")
else:
    print("ALEMANHA")