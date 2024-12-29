my_list = []
swapped = True
num = int(input("Quantos elementos você deseja embaralhar? "))

for i in range(num):
 val = float(input("Entre com a lista de elementos:"))
 my_list.append(val)

while swapped:
    swapped = False #assume que existe a chance da lista ja estar correta
    for i in range(len(my_list) - 1): #para cada item dentro do numero de itens da minha lista menos 1
        if my_list[i] > my_list[i + 1] : #se o item atual for maior que o posterior
            swapped = True #quer dizer que ocorreu uma troca
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] #realiza a troca

print("\nSorted:")
print(my_list)

# metodo mais rapido = .sort()
second_list = [7, 3, 5, 9, 11]
second_list.sort() #função para organizar de maneira rapida
print(second_list)

# funciona com strings tambem
lst = ["D", "F", "A", "Z"]
lst.sort()
 
print(lst)

# posso fazer desta maneira tambem, reversa
a = "A"
b = "B"
c = "C"
d = " "
 
lst1 = [a, b, c, d]
lst1.reverse()
 
print(lst1)
 

