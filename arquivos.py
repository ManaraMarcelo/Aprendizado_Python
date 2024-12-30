'''1. Arquivos TXT
O que é?
Arquivos de texto simples que armazenam dados em formato bruto (plain text).

Operações comuns:

Abrir um arquivo: Usando a função open().
Ler um arquivo: Métodos como read() ou readlines().
Escrever em um arquivo: Usando write().
Exemplo:'''

# Escrevendo em um arquivo TXT
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\nBem-vindo ao Python.")

# Lendo um arquivo TXT
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
'''2. Arquivos CSV
O que é?
Arquivos com valores separados por vírgulas (Comma-Separated Values), geralmente usados para armazenar tabelas de dados.

Biblioteca necessária: csv (nativa do Python).

Operações comuns:

Ler um CSV: Usando csv.reader().
Escrever em um CSV: Usando csv.writer().
Exemplo:'''

import csv

# Escrevendo em um arquivo CSV
with open("exemplo.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Idade", "Cidade"])
    escritor.writerow(["Marcelo", 20, "São Paulo"])
    escritor.writerow(["Ana", 25, "Rio de Janeiro"])

# Lendo um arquivo CSV
with open("exemplo.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

'''Os modos de abertura são passados como argumentos para a função open() e determinam como o arquivo será manipulado.

Modos Comuns:
Leitura (r)

Abre o arquivo apenas para leitura.
O arquivo deve existir; caso contrário, ocorre um erro.'''

with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
'''Escrita (w)

Abre o arquivo para escrita, sobrescrevendo seu conteúdo.
Se o arquivo não existir, ele será criado.'''

with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Novo conteúdo.")
'''Anexar (a)

Abre o arquivo para adicionar conteúdo ao final.
Se o arquivo não existir, ele será criado.'''

with open("arquivo.txt", "a") as arquivo:
    arquivo.write("Conteúdo adicional.\n")
'''Leitura/Escrita (r+)

Abre o arquivo para leitura e escrita.
O arquivo deve existir; caso contrário, ocorre um erro.'''

with open("arquivo.txt", "r+") as arquivo:
    arquivo.write("Conteúdo editado.")
'''Escrita/Leitura (w+)

Abre o arquivo para leitura e escrita, sobrescrevendo seu conteúdo.
Se o arquivo não existir, ele será criado.'''

with open("arquivo.txt", "w+") as arquivo:
    arquivo.write("Novo conteúdo.")
    arquivo.seek(0)
    print(arquivo.read())

'''Anexar/Leitura (a+)

Abre o arquivo para leitura e para adicionar conteúdo ao final.
Se o arquivo não existir, ele será criado.'''

with open("arquivo.txt", "a+") as arquivo:
    arquivo.write("Conteúdo adicional.\n")
    arquivo.seek(0)
    print(arquivo.read())

'''Modos para Arquivos Binários
Use o sufixo b para manipular arquivos binários (imagens, vídeos, etc.).'''

#Leitura Binária (rb)

with open("imagem.jpg", "rb") as arquivo:
    dados = arquivo.read()

#Escrita Binária (wb)

with open("imagem_copia.jpg", "wb") as arquivo:
    arquivo.write(dados)
    
'''Leitura/Escrita Binária (rb+, wb+, ab+)

Funcionam como os modos texto (r+, w+, a+), mas para arquivos binários.'''
