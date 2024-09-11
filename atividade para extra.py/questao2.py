numero = []
for i in range(8):
    num = float(input(f"Algarismo {i + 1}: "))
    numero.append(num)

negativo = 0
soma_positivo = 0

for num in numero:
    if num < 0:
        negativo +=1
    elif num > 0:
        soma_positivo += num
print(f"Números negativos: {negativo}")
print(f"Soma dos números positivos: {soma_positivo}")
