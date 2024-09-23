#criar um dicionário, é basicamente ima lista com indice textual

pessoa = {
    'Nome':'Maria',
    'Idade':20,
    'Endereço':'Avenida 23'
}
print(pessoa)

#Exibindo as chaves utilizando o comando keys()
print(pessoa.keys()) 

#Exibindo os valores utilizando o comando values()
print(pessoa.values())

#Exibindo tanto a chave quanto o valor 
print(pessoa.items())

for chave, valor in pessoa.items():
    print(f"{chave} : {valor}") 

#REALIZANDO OPERAÇOES COM DICIONÁRIO 
#Adicionando dados
#Forma 1
pessoa["Peso"] = 68
print(pessoa)

#Forma 2 - usando update()
pessoa.update({"profissão" :"Diretora"})

#removendo dados do dicionário 
#forma 1 - pop()
pessoa.pop()
pessoa.pop("peso")
print(pessoa)

#forma 2 - del()
del(pessoa["Endereço"])
print(pessoa)