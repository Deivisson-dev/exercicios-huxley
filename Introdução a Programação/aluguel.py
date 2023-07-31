dias = int(input())
km = int(input())

kmrodado = 0.01 * km
total = (30*dias) + kmrodado
total_bonus = total - (total/10)

print("{:.2f}".format(round(total_bonus, 2)))