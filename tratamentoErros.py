"""
O bloco try e except em Python é usado para tratar exceções, ou seja, erros que
podem ocorrer durante a execução do código. Quando você espera que algo possa gerar um
erro e deseja evitar que o programa pare de funcionar, você pode envolver esse código
em um bloco try e, em caso de erro, ele será tratado dentro do bloco except.
"""

try:
    numerador = int(input("Digite o numerador: "))
    denominador = int(input("Digite o denominador: "))
    resultado = numerador / denominador
    print(f"O resultado é {resultado}")
except ValueError:  #será tratado se o usuário digitar algo que não pode ser convertido para um número.
    print("Erro: Você deve digitar números inteiros!")
except ZeroDivisionError:  #será tratado se o usuário tentar dividir por zero.
    print("Erro: Divisão por zero não é permitida!")


try:
    numero = int(input("Digite um número: "))
    print(f"Você digitou o número {numero}")
except ValueError:
    print("Erro: Isso não é um número válido!")
except:   # excessão padrão, quando ocorre algum erro não identificado ele se enquadra neste tratamento
    print('algo de estranho aconteceu aqui ... Desculpe! ')
else:   # posso usar como forma de confirmação de que ocorreu tudo bem no meu teste
    print("Nenhum erro ocorreu, tudo certo!")
finally:   # sempre será executado
    print("Isso sempre será executado, independentemente de erros.")
