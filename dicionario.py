dicionarioProdutos = {"Macbook": 7000, "Iphone14": 3500, "AirpodsPro": 2500, "Ipad": 5000} #posso adicionar um rótulo e um valor indexado

#pegar um elemento 
print(dicionarioProdutos["Iphone14"])

#editar um elemento
dicionarioProdutos["AirpodsPro"] = dicionarioProdutos["AirpodsPro"] *1.6
print(dicionarioProdutos)

#retirar um item do dicionário
dicionarioProdutos.pop("Ipad")
print(dicionarioProdutos)

#adicionar item no dicionario
dicionarioProdutos["Icloud"] = 200 #é igual a editar, porem se não existir o elemento ele adiciona
print(dicionarioProdutos)

#quantidade de itens dentro do dicionário
print(len(dicionarioProdutos))

nomeProduto = input("Digite o nome do produto: ")
nomeProduto = nomeProduto.lower 
precoProduto = input("Digite o valor do produto: ")
precoProduto = float(precoProduto)

