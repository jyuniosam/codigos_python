numeros = []
divisores = []

for contador in range(1,6):
    number = int(input('Digite um valor: '))
    numeros.append(number)
print(f'Lista completa: {numeros}')
for itens in numeros:
if itens % 3 == 0:
