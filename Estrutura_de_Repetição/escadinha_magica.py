n = int(input())
for i in range(1, n + 1):
    for k in range(1, i):
        print(k, end=' ')
    print(i)