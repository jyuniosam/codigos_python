import random

def gerar_numeros_aleatorios(inicio, fim):
    return random.randint(inicio, fim)

def main():
    numeros_aleatorios = []

    for _ in range(5):  # Permitir 5 operações
        try:
            inicio = int(input("Digite o limite inferior: "))
            fim = int(input("Digite o limite superior: "))
            
            if inicio > fim:
                print("O limite inferior deve ser menor ou igual ao limite superior.")
                continue

            numero_gerado = gerar_numeros_aleatorios(inicio, fim)
            numeros_aleatorios.append(numero_gerado)
            print(f"Número aleatório gerado: {numero_gerado}")
        
        except ValueError:
            print("Por favor, insira números inteiros válidos.")

    print("\nLista de números aleatórios gerados:", numeros_aleatorios)


