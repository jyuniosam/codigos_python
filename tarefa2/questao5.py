import random

def main():
    # Lista que contém os possíveis resultados do lançamento da moeda
    resultados = []
    opcoes = ["Cara", "Coroa"]

    while True:
        # Simula o lançamento da moeda
        resultado = random.choice(opcoes)
        resultados.append(resultado)
        print(f"Resultado do lançamento: {resultado}")

        # Pergunta ao usuário se deseja lançar a moeda novamente
        continuar = input("Deseja lançar a moeda novamente? (s/n): ").strip().lower()
        
        if continuar != 's':
            break

    # Exibe a lista com todos os resultados
    print("\nResultados dos lançamentos:")
    for i, resultado in enumerate(resultados, start=1):
        print(f"Lançamento {i}: {resultado}")

# Chama a função principal
if __name__ == "__main__":
    main()
