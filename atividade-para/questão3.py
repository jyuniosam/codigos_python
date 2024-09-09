# Solicitar ao usuário que insira um número inteiro 
numero = int(input("Digite um número: "))

#Verificar e exibir todos os divisores do número
print(f"Divisores de {numero}:")

# Encontrar divisores
for contador in range(1, (numero) +1):
    if numero % contador ==0:
        print(contador)