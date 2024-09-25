import time

def contagem_regressiva(segundos):
    while segundos >= 0:
        print(segundos)
        time.sleep(1)  # Pausa de 1 segundo
        segundos -= 1
    print("Tempo esgotado!")

def main():
    segundos = int(input("Digite o número de segundos para a contagem regressiva: "))
    contagem_regressiva(segundos)
