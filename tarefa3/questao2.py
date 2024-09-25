import random

def mostrar_moedas(cotacoes):
    print("\nMoedas disponíveis para conversão:")
    for moeda, valor in cotacoes.items():
        print(f"{moeda}: R$ {valor:.2f}")

def converter_moeda(cotacoes, valor_reais, moeda_escolhida):
    taxa = cotacoes[moeda_escolhida]
    valor_convertido = valor_reais / taxa
    return valor_convertido

def main():
    cotacoes = {
        "Dólar": 5.30,    # Cotação aproximada
        "Euro": 5.60,     # Cotação aproximada
        "Libra Esterlina": 6.50,  # Cotação aproximada
        "Iene": 0.04,     # Cotação aproximada
        "Franco Suíço": 5.80,  # Cotação aproximada
    }

    for _ in range(5):  # Permitir 5 operações
        mostrar_moedas(cotacoes)
        
        moeda_escolhida = input("Escolha uma moeda para conversão (digite o nome): ")
        
        if moeda_escolhida not in cotacoes:
            print("Moeda inválida! Tente novamente.")
            continue
        
        valor_reais = float(input("Digite o valor em reais: R$ "))
        
        valor_convertido = converter_moeda(cotacoes, valor_reais, moeda_escolhida)
        print(f"{valor_reais:.2f} R$ equivalem a {valor_convertido:.2f} {moeda_escolhida}.")

        continuar = input("Deseja fazer outra conversão? (s/n): ").lower()
        if continuar != 's':
            print("Programa encerrado.")
            break

