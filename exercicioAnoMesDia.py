def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
# Lista com o número de dias em cada mês (para anos não bissextos)
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verifica se o mês é válido
    if month < 1 or month > 12:
        return None
    
    # Verifica se o ano é bissexto e ajusta fevereiro
    if is_year_leap(year) and month == 2:
        return 29
    
    # Retorna o número de dias do mês
    return days_in_month_list[month - 1]

def day_of_year(year, month, day):
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verifica se o mês é válido
    if month < 1 or month > 12:
        return None
    
    # Verifica se o ano é bissexto e ajusta fevereiro
    if is_year_leap(year) and month == 2:
        return 29
    
    # Retorna o número de dias do mês
    return days_in_month_list[month - 1]

    if year < 0:
        return None
    
    

print(day_of_year(2000, 12, 31))