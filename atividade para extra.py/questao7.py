a = int(input("Digite o primeiro número inteiro positivo: "))
b = int(input("Digite o segundo número inteiro positivo: "))

contador = 0

for num in range(a, b + 1):
    if num % 7 == 0 and num % 11 == 0:
        contador += 1

print(f"O total de números entre {a} e {b} que são múltiplos de 7 e 11 simultaneamente é:{contador}")
