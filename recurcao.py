# a funcao se chama -----------------
#Fibonacci
def fibonacci(n):
    if n < 1:
        return None
    if n < 3: 
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))

#fatorial como exemplo
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)
 
print(factorial_function(8))