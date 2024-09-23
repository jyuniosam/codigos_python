valor = []

for contador in range (1,7):
    numero = int(input("Digite seis números:" )) 
    valor.append (numero)
    print(valor)

while True: 
    posiçao1 = int(input("Escolha a primeira posição do número: "))
    posiçao2 = int(input("Escolha a segunda posição do número: "))

     
    if 0 <= posiçao1 < 6 and 0 <= posiçao2 < 6:
        break
    else:
     print("Posições inválidas. As posições devem estar entre 1 e 7.")

     posiçao1 = valor[posiçao1]
     posiçao2 = valor[posiçao2]

print("-"*50)
produto = posiçao1 * posiçao2
print(f"O produto dos números é {produto}")

soma = posiçao1 + posiçao2
print(f"A soma dos números é {soma}")

diferença = posiçao1 - posiçao2
print(f"A diferença dos números é {diferença}")

divisao = posiçao1 / posiçao2
print(f"A divisão dos números é: {divisao}")

exponenciacao = posiçao1 ** posiçao2
print(f"A exponenciação dos números é: {exponenciacao}")
