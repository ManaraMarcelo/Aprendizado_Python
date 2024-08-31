listaVazia = []

listaVazia.append("Olá")  # O .append serve para somar termos
listaVazia.append("Mundo")

print(listaVazia)

numeros = [10, 9, 8, 7]

print("Total de números: ", len(numeros))
print("Maior número: ", max(numeros))
print("Menor número: ", min(numeros))


lista = [1, 2, 3, 4, 5, 6]
midleNumber = len(lista)//2

print(midleNumber)
lista[2] = int(input("Insira o valor do meio da lista: "))
print(lista)
print(midleNumber)

del lista[-1] #negativo = ultimo numero 
del lista[0] #primerito numero 
print(lista)
lista.insert(4, int(input("Insira o valor que deseja no indice 4: "))) #insere valor onde eu quiser na lista
print("Lista atualizada = ", lista) #print(location, value)
lista.append(66) #insere apenas no final da lista
print("Lista atualizada = ", lista)

