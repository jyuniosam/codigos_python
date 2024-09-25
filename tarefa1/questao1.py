def calcular_calorias(atividade, tempo):
    if atividade == 'caminhada':
        return tempo * 5
    elif atividade == 'corrida':
        return tempo * 10
    elif atividade == 'ciclismo':
        return tempo * 8    
    else:
        return None

def main():
    print("Calcule as calorias queimadas em atividades físicas!")
    
    atividade = input("Informe o tipo de atividade (caminhada, corrida, ciclismo): ").lower()
    tempo = int(input("Informe o tempo em minutos: "))
    
    calorias = calcular_calorias(atividade, tempo)
    
    if calorias is not None:
        print(f"Você queimou {calorias} calorias ao fazer {atividade} por {tempo} minutos.")
    else:
        print("Atividade inválida! Por favor, escolha entre caminhada, corrida ou ciclismo.")
