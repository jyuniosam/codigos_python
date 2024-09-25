import random

def mostrar_cardapio(cardapio):
    print("\nCardápio:")
    for prato, preco in cardapio.items():
        print(f"{prato}: R$ {preco:.2f}")
    print()

def adicionar_prato(cardapio):
    prato = input("Digite o nome do prato a ser adicionado: ")
    preco = float(input("Digite o preço do prato: R$ "))
    cardapio[prato] = preco
    print(f"{prato} adicionado com sucesso!")

def remover_prato(cardapio):
    prato = input("Digite o nome do prato a ser removido: ")
    if prato in cardapio:
        del cardapio[prato]
        print(f"{prato} removido com sucesso!")
    else:
        print("Prato não encontrado!")

def consultar_preco(cardapio):
    prato = input("Digite o nome do prato que deseja consultar: ")
    if prato in cardapio:
        print(f"O preço de {prato} é: R$ {cardapio[prato]:.2f}")
    else:
        print("Prato não encontrado!")

def main():
    cardapio = {
        "Pizza Margherita": 29.90,
        "Hambúrguer": 19.90,
        "Salada Caesar": 24.90,
        "Espaguete à Carbonara": 34.90,
        "Tacos": 22.90,
    }

    operacoes = {
        "1": adicionar_prato,
        "2": remover_prato,
        "3": consultar_preco,
        "4": mostrar_cardapio,
        "5": exit,
    }

    for _ in range(5):  # Permitir 5 operações
        print("\nEscolha uma operação:")
        print("1 - Adicionar prato")
        print("2 - Remover prato")
        print("3 - Consultar preço")
        print("4 - Exibir cardápio completo")
        print("5 - Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao in operacoes:
            operacoes[opcao](cardapio)
        else:
            print("Opção inválida! Tente novamente.")


