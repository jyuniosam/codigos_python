#1ª forma de ultilizar while - semelhante ao FOR contador = 1 

contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1 # é o mesmo que contador +=1


print("="*40)
    #2ª forma de utilizar enquanto - loop condicionl normal 
valor = 0 

while valor >= 0:
    valor = int(input("informe um valor qualquer(digite um valor negativo para terminar: )"))

    print(f"você digitou {valor}")

print("="*40)
    #3ª forma de utilizar o enquanto - semelhante a estrutura faça..enquanto sxt  

while True:
    senha = input("informe sua senha: ")

    if senha == "123":
        print("parabéns, senha correta")
        break # forma de encerrar o loop
    else:
            print("senha não conferem tente novamente")
