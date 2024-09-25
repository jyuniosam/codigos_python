def main():
    eventos = []
    
    while True:
        print("\nMenu de Gerenciamento de Eventos")
        print("1. Adicionar um novo evento")
        print("2. Remover um evento")
        print("3. Exibir eventos")
        print("4. Sair")
        
        escolha = input("Escolha uma opção (1-4): ")
        
        if escolha == '1':
            evento = input("Digite o nome do evento para adicionar: ")
            eventos.append(evento)
            print(f"Evento '{evento}' adicionado com sucesso!")
        
        elif escolha == '2':
            if not eventos:
                print("Nenhum evento para remover.")
            else:
                print("Eventos atuais:")
                for i, evento in enumerate(eventos, start=1):
                    print(f"{i}. {evento}")
                
                posicao = int(input("Qual a posição do evento a ser removido? "))
                
                if 1 <= posicao <= len(eventos):
                    evento_removido = eventos.pop(posicao - 1)
                    print(f"Evento '{evento_removido}' removido com sucesso!")
                else:
                    print("Posição inválida.")
        
        elif escolha == '3':
            if eventos:
                print("\nEventos Agendados:")
                for i, evento in enumerate(eventos, start=1):
                    print(f"{i}. {evento}")
            else:
                print("Nenhum evento agendado.")
        
        elif escolha == '4':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 4.")

# Chama a função principal
if __name__ == "__main__":
    main()
