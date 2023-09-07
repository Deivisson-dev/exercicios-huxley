m = int(input())
n = int(input())
multiplos = []
for i in range(1, n+1):
    if i % m == 0:
        multiplos.append(i)

if len(multiplos) == 0:
    print(f"sem multiplos menores que {n}")
else:
    print(multiplos[-1])