def main():
    # Lê a primeira lista de números inteiros
    lista1 = input("Digite a primeira lista de números inteiros, separando-os por espaço: ")
    lista1 = list(map(int, lista1.split()))
    
    # Lê a segunda lista de números inteiros
    lista2 = input("Digite a segunda lista de números inteiros, separando-os por espaço: ")
    lista2 = list(map(int, lista2.split()))
    
    # Encontra a interseção
    intersecao = set(lista1) & set(lista2)
    
    # Ordena a interseção
    intersecao_ordenada = sorted(intersecao)
    
    # Exibe os números comuns
    print("Números comuns:", intersecao_ordenada)

# Chama a função principal
if __name__ == "__main__":
    main()
