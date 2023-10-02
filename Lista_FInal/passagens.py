voos = {}

for i in range(37):
    numero_lugares = input().split()
    numero = numero_lugares[0]
    lugares = numero_lugares[1]
    voos[numero] = lugares

while True:
    numidentidade_numvoo = input().split()
    numidentidade = numidentidade_numvoo[0]
    if numidentidade == '9999':
        break
    numvoo = numidentidade_numvoo[1]
    if numvoo in voos:
        if int(voos[numvoo]) > 0:
            voos[numvoo] = int(voos[numvoo]) - 1
            print(numidentidade)
        else:
            print("INDISPONIVEL")
    else:
        print("INDISPONIVEL")