nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário: "))

if salario < 3000:
    print("Você é um programador Júnior...")
elif salario > 3000 and salario <= 6000:
    print("Você é um programador Pleno")
elif salario > 6000 and salario <= 15000:
    print("Você é um programador Sênior")
else:
    print("Você é um Gerente de Projetos!")

print("End")
