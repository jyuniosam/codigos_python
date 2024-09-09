# Inicializar o contador para pessoas com 18 anos 
contador_maior_igual_18 = 0 

# Solicitar a idade de 5 pessoas 
for idade in range(1,6):
idadee = int(input(f"Digital a idade da pessoa {idade}: "))
# Verificar se a idade é maior ou igual a 18 
if idade >= 18:
    contador_maior_igual_18 += 1 

    #Mostrar o resultado  
    print(f"Quantidade de pessoas com 18 anos ou mais: {contador_maior_igual_18}")