import os

MAX_PRODUTOS = 100  # Define o número máximo de produtos no estoque

# Classe que representa um Produto
class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id  # ID único do produto
        self.nome = nome  # Nome do produto
        self.preco = preco  # Preço do produto
        self.quantidade = quantidade  # Quantidade no estoque

# Função para adicionar um novo produto ao estoque
def adicionar_produto(produtos):
    if len(produtos) < MAX_PRODUTOS:
        id = int(input("ID do produto: "))
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade no estoque: "))

        # Adiciona o novo produto à lista de produtos
        novo_produto = Produto(id, nome, preco, quantidade)
        produtos.append(novo_produto)
    else:
        print("Estoque cheio!")

# Função para atualizar um produto existente
def atualizar_produto(produtos):
    id = int(input("Digite o ID do produto a ser atualizado: "))
    encontrado = False

    for produto in produtos:
        if produto.id == id:
            produto.preco = float(input("Novo preço: "))
            produto.quantidade = int(input("Nova quantidade: "))
            encontrado = True
            break

    if not encontrado:
        print("Produto não encontrado!")

# Função para listar todos os produtos no estoque
def listar_estoque(produtos):
    for produto in produtos:
        print(f"ID: {produto.id}")
        print(f"Nome: {produto.nome}")
        print(f"Preço: {produto.preco:.2f}")
        print(f"Quantidade: {produto.quantidade}\n")

# Função para salvar o estoque em um arquivo
def salvar_estoque(produtos):
    with open("estoque.txt", "w") as arquivo:
        for produto in produtos:
            arquivo.write(f"{produto.id} {produto.nome} {produto.preco} {produto.quantidade}\n")
    print("Estoque salvo com sucesso!")

# Função para carregar o estoque de um arquivo
def carregar_estoque():
    produtos = []
    if os.path.exists("estoque.txt"):
        with open("estoque.txt", "r") as arquivo:
            for linha in arquivo:
                id, nome, preco, quantidade = linha.split()
                produtos.append(Produto(int(id), nome, float(preco), int(quantidade)))
    else:
        print("Nenhum arquivo de estoque encontrado. Iniciando novo estoque.")
    return produtos

# Função principal do programa
def main():
    produtos = carregar_estoque()
    opcao = 0

    while opcao != 4:
        print("\nMenu:")
        print("1. Adicionar Produto")
        print("2. Atualizar Produto")
        print("3. Listar Estoque")
        print("4. Salvar Estoque e Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            adicionar_produto(produtos)
        elif opcao == 2:
            atualizar_produto(produtos)
        elif opcao == 3:
            listar_estoque(produtos)
        elif opcao == 4:
            salvar_estoque(produtos)
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
