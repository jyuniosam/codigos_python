valor_inicial = int(input("Digite o valor inicial:"))
valor_final = int(input("Digite o valor final"))
soma = 0 #variável que vai armazenar a soma 

# Calcular a soma dos números inteiros no intervalo [valor_inicial, valor_final]
for numero in range(valor_inicial, valor_final +1):
    soma += numero
print (f"A soma dos números inteiros entre {valor_inicial} e {valor_final} é: {soma}")