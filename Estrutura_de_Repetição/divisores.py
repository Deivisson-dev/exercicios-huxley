n = int(input())
divisores = []
for i in range(n+1, 0, -1):
    if n % i == 0:
        divisores.append(i)

for j in divisores:
    print(j)