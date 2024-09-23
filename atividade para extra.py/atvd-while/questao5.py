import random
valores = {i:0 for i in range(1,7)}

for _ in range(10):
    resultado = random.randint(1,6)
    valores[resultado] += 1

for valor, quantidade in valores.items():
    print(f"o valor {valor} foi sorteado {quantidade} vezes")