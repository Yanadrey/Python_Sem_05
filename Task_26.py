# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую 
# степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a = int(input("Введите основание степени: "))
b = int(input("Введите показатель степени: "))

def in_degree(basis,indicator):
    if indicator==1:
        return basis
    return(basis*in_degree(basis,indicator-1))
    
print(f"Число {a} в степени {b} равно {in_degree(a,b)}.")    