def calcular_gorjeta(valor_conta, percentual_gorjeta):
    gorjeta = valor_conta * (percentual_gorjeta / 100)
    total = valor_conta + gorjeta
    return gorjeta, total

def main():
    print("Cálculo de Gorjeta em Restaurante")
    
    # Entrada do valor da conta
    valor_conta = float(input("Informe o valor da conta (R$): "))
    
    # Entrada do percentual de gorjeta
    percentual_gorjeta = float(input("Informe o percentual de gorjeta (ex: 10, 15, 20): "))
    
    # Cálculo da gorjeta e total
    gorjeta, total = calcular_gorjeta(valor_conta, percentual_gorjeta)
    
    # Exibição dos resultados
    print(f"Gorjeta: R$ {gorjeta:.2f}")
    print(f"Total: R$ {total:.2f}")
