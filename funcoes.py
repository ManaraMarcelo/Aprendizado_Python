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

def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # É divisível por 400, é bissexto
            else:
                return False  # Divisível por 100 mas não por 400, não é bissexto
        else:
            return True  # Divisível por 4, mas não por 100, é bissexto
    else:
        return False  # Não é divisível por 4, não é bissexto

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1] #Se month = 1 (janeiro), days[1 - 1] = days[0], que é o primeiro item da lista (31 dias).
    if month == 2 and is_year_leap(year):
        res = 29
    return res

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fracassado")

#funcoes multiparametricas --------------------------

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    else:
        return weight / height**2
    
print(bmi(352.5, 1.65))
print(bmi(180.5, 1.6))

#fatorial ---------------------------------

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
 
for n in range(1, 6):  # testando
    print(n, factorial_function(n))
 
