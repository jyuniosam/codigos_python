import random

def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate!"
    elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
        return "Você ganhou!"
    else:
        return "Computador ganhou!"
    

def main():
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    
    while True:
        print("\nEscolha uma opção:")
        print("1: Pedra")

        print("2: Papel")
        print("3: Tesoura")

        jogador = int(input("Faça sua escolha (1, 2 ou 3): "))
        
        # Geração da escolha do computador
        computador = random.randint(1, 3)
        
        # Mapeamento para as escolhas
        opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
        
        print(f"\nVocê escolheu: {opcoes[jogador]}")
        print(f"Computador escolheu: {opcoes[computador]}")  
        
        # Determinar o vencedor
        resultado = determinar_vencedor(jogador, computador)
        print(resultado)
        
        # Perguntar se o usuário deseja jogar novamente
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            break


