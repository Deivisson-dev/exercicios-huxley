n1 = int(input())
n2 = int(input())
multiplos = []
for i in range(1, 50):
    if i % n1 == 0 and i % n2 == 0:
        multiplos.append(i)
print(len(multiplos))