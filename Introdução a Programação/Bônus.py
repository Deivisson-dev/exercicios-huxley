nome = input()
sal = float(input())
vendas = float(input())

tot = sal + vendas * 0.15


print("TOTAL = R$ {:.2f}".format(round(tot, 2)))