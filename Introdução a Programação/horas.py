segundos = int(input())

horas = segundos // 3600
segundos_rest = segundos % 3600
minutos = segundos_rest// 60
segundos = segundos_rest % 60



print(f"{horas} h {minutos} m {segundos} s")
