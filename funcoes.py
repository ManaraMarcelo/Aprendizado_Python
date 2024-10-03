def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(2))
print(strange_function(1)) #se não é passado parametro para a excessão, ele irá printar NONE
 

def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s
 
print(list_sum([5, 4, 3]))
print(len(lst))
 
