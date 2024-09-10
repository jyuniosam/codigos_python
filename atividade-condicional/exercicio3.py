salario = float(input("informe seu sálario: "))
financiamento = float(input("informe o financiamento pretendido: "))

if financiamento <=5 * salario:
    print(f"financiamento concedido\n")

else:
    print(f"financiamento negado\n")

print(f"obrigado por nos consultar\n")