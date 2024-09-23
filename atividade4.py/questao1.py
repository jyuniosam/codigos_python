Itens = []
# preenchendo a lista
while True:
    valor = int(input("Informe um valor numérico"))     
    if valor == 0:
        break
else:
     itens.append(valor)
print(itens)

#pecorrer a lista
for contador in itens:
    if contador == 3:
        itens.remove(contador)  
    print(itens)      