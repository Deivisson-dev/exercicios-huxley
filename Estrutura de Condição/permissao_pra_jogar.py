idade = int(input())
tipo_jogo = input()

if idade < 0 or idade > 130:
    print("Idade invalida.")
elif tipo_jogo != "azar" and tipo_jogo != "mmorpg" and tipo_jogo != "moba" and tipo_jogo != "casual":
    print("Jogo invalido.")
else:
    if tipo_jogo == "azar" and idade >= 21:
        print("Pode entrar!")
    elif tipo_jogo == "azar" and idade < 21:
        print("Volte daqui há alguns anos.")
    elif tipo_jogo == "mmorpg" and idade >= 14:
        print("Pode entrar!")
    elif tipo_jogo == "mmorpg" and idade < 14:
        print("Volte daqui há alguns anos.")
    elif tipo_jogo == "moba" and idade >= 10:
        print("Pode entrar!")
    elif tipo_jogo == "moba" and idade < 10:
        print("Volte daqui há alguns anos.")
    elif tipo_jogo == "casual" and idade >= 0 and idade <= 130:
        print("Pode entrar.")