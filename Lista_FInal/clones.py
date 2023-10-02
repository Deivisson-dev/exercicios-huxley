while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    pessoas_dna = {}

    for i in range(n):
        seq_dna = input()
        if seq_dna in pessoas_dna:
            pessoas_dna[seq_dna] += 1
        else:
            pessoas_dna[seq_dna] = 1

    
    counts = [0] * (n + 1)

    for _, count in pessoas_dna.items():
        if count <= n:
            counts[count] += 1

    for count in counts[1:]:
        print(count)
