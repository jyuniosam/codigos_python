import random

def converter_temperatura(celsius, escala):
    if escala == 'F':
        return (9/5) * celsius + 32
    elif escala == 'K':
        return celsius + 273.15
    else:
        return None

def main():
    for _ in range(5):  # Permitir 5 operações
        celsius = float(input("Digite a temperatura em graus Celsius (ou um valor negativo para sair): "))
        if celsius < 0:
            print("Programa encerrado.")
            break
        
        print("Escolha a escala para conversão:")
        print("F - Fahrenheit")
        print("K - Kelvin")
        escala = input("Digite 'F' ou 'K': ").upper()

        if escala not in ['F', 'K']:
            print("Escala inválida! Tente novamente.")
            continue

        temperatura_convertida = converter_temperatura(celsius, escala)

        if escala == 'F':
            print(f"{celsius:.2f} °C equivalem a {temperatura_convertida:.2f} °F.")
        elif escala == 'K':
            print(f"{celsius:.2f} °C equivalem a {temperatura_convertida:.2f} K.")

    
