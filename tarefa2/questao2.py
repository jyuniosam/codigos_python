def main():
    notas = []
    
    # Coleta de notas
    while True:
        nota = float(input("Digite a nota do aluno (ou 0 para terminar): "))
        if nota == 0:
            break
        notas.append(nota)
    
    # Calcula a quantidade de alunos com notas acima da média (7)
    media = 7
    alunos_acima_da_media = sum(1 for nota in notas if nota > media)
    
    # Exibe o resultado
    print(f"Número de alunos com notas acima da média (7): {alunos_acima_da_media}")

# Chama a função principal
if __name__ == "__main__":
    main()
