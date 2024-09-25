import random

def main():
    # Escolha uma lista de palavras
    lista_opcoes = {
        1: ['leão', 'tigre', 'elefante', 'girafa', 'zebra', 'macaco', 'panda', 'hipopotamo', 'leopardo', 'canguru', 'urso', 'coelho', 'cavalo', 'pinguim', 'lobo'],
        2: ['maçã', 'banana', 'laranja', 'morango', 'uva', 'abacaxi', 'kiwi', 'manga', 'pera', 'melancia', 'framboesa', 'nectarina', 'carambola', 'figo', 'amora'],
        3: ['Brasil', 'Canadá', 'Japão', 'Austrália', 'França', 'Índia', 'México', 'Itália', 'Egito', 'Argentina', 'Alemanha', 'China', 'Itália', 'Reino Unido', 'Noruega'],
        4: ['vermelho', 'azul', 'verde', 'amarelo', 'laranja', 'roxo', 'rosa', 'marrom', 'preto', 'branco', 'cinza', 'turquesa', 'bege', 'lilás', 'prata'],
        5: ['futebol', 'basquete', 'natação', 'tênis', 'vôlei', 'corrida', 'rugby', 'golfe', 'ciclismo', 'boxe', 'esgrima', 'handebol', 'karate', 'skate', 'surfe']
    }

    print("Escolha uma categoria de palavras:")
    print("1. Animais")
    print("2. Frutas")
    print("3. Países")
    print("4. Cores")
    print("5. Esportes")

    categoria = int(input("Digite o número da categoria (1-5): "))
    palavras = lista_opcoes[categoria]

    # Embaralha a lista de palavras
    random.shuffle(palavras)

    # Escolhe uma palavra aleatória
    palavra_escolhida = random.choice(palavras)
    indice_palavra = palavras.index(palavra_escolhida)

    print(f"\nA lista de palavras foi embaralhada e não será mais mostrada.")
    print(f"A lista começa com a posição 0 e vai até 14.")

    tentativas = 3

    while tentativas > 0:
        palpite = int(input(f"Em qual posição se encontra a palavra '{palavra_escolhida}'? (Tentativas restantes: {tentativas}) "))
        
        if palpite == indice_palavra:
            print("Parabéns! Você acertou!")
            break
        else:
            tentativas -= 1
            print(f"Você errou. Você ainda tem {tentativas} tentativas restantes.")

    if tentativas == 0:
        print(f"Você não acertou. A palavra estava na posição {indice_palavra}.")

    print("\nLista de palavras embaralhada:")
    for i, palavra in enumerate(palavras):
        print(f"{i}: {palavra}")

# Chama a função principal
if __name__ == "__main__":
    main()
