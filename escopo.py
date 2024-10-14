# Existe a possibilidade de tornar variaveis de dentro e fora de funções com o mesmo valor

def my_function():
    global  var # crio uma variavel global dentro da função 
    var = 2
    print("Valor: ", var)

var = 1
print(var)
my_function()
print(var)
