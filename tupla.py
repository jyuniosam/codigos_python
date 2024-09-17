objetos = ('Lapis' , 'Borracha' , 'Caderno')
print(objetos[1]) #Irei exibir o intem na posição 1, ou seja segunda posição, uma vez que toda coleção começa na posição zero.

print(type(objetos))# irá mostrar o tipo da variável

print(objetos) #exibindo todos os intens de uma só vez 

print("-"*50)
for item in range(0,3):
    print(objetos[item])# exibindo todos os itens da tupla 
    
    #Exibindo todos os itens da tupla sema função range 
   print("")
    print("-"*50)
    for elementos in objetos:
        print(elementos)

        #iremos tentar alterar o contéudo da tupla 
        objetos[0] = "Caneta"
    