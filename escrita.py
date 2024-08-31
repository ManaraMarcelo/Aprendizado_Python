# Definindo as variáveis
faturamento = 1200
lucro = 5
valorLiquido = faturamento * lucro
YourName = "Manara"

# Imprimindo os valores com formatação
print(f"Faturamento = {faturamento}, Lucro = {lucro}, Valor Líquido = {valorLiquido}")

print(f"Seu lucro: {lucro}")
print(f"Your name is: {YourName.upper() + '!' * 3}")  # tudo maiúsculo
print(f"Your name lower is: {YourName.lower() + '!' * 3}")  # tudo minúsculo

# localizar índice dentro do texto
emailCliente = "manarinha@gmail.com"
print(emailCliente)
print(emailCliente.find("@")) #vai retornar -1 se não encontrar nada

#quantidade de caracteres dentro do texto
print(len(emailCliente)) #lembrando que começa do zero

#pegar um caractere pelo índice
print(emailCliente[6])
print(emailCliente[-4]) #conta de trás para frente

#pegar um pedaço do texto
print(emailCliente[1:7])
print(emailCliente[5:]) #se eu não denotar um final ele vai até o último

#trocar pedaço do texto 
novoEmail = emailCliente.replace("gmail.com", "hotmail.com") #se ele não encontrar nada ele não vai avisar
print(emailCliente)
print(novoEmail)
      
#formatar texto
nome = "marcelo augusto manara de abreu"

print(nome.capitalize()) #deixa apenas a primeira letra do texto maiúscula
print(nome.title()) #deixa todas as primeiras letras do texto maiúsculas

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
