listaVendas = [1000, 200, 1500]

meta = 1200
percentualBonus = 0.1

for venda in listaVendas: #para cada venda dentro da lista de vendas faça: 
    if venda >= meta:
        bonus = percentualBonus * venda
    else:
        bonus = 0
    
    print("Seu bônus é: ", bonus)

print("End Code.")

#--------------------------------------------------------------------------

import time

for i in range(5):
    number = i+1
    print(str(number) +" Mississipi")
    time.sleep(1)

print("Read or not, I'm here.")

#-----------------------------------------------------------

userword = input("Digite a palavra chave: ")
userword = userword.upper()

vowels = "AEIOU"

for letter in userword:
    if letter in vowels:
        continue

    print(letter)

# ------------------------------------

#range(start, stop, step)
for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

# -----------------------------------

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i) #o indice 0 faz com que seja sempre adicionado no inicio, empurrando os anteriores para a direita.
    
    return strange_list

print(strange_list_fun(5))

