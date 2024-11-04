#Ejercicio 9

#El número de Euler, e ≈ 2,71828, puede ser representado como la siguiente suma infinita:

#e=10!+11!+12!+13!+14!+…
#Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.
#
#Recuerde que el factorial n! es el producto de los números de 1 a n.


import math


def calcular_euler():
    suma = 0
    n = 10  
    
    while True:
        
        factorial = math.factorial(n)
        
        
        suma += factorial
        
        
        siguiente_factorial = math.factorial(n + 1)
        diferencia = abs(siguiente_factorial - factorial)
        
        
        print(f"n: {n}, Factorial: {factorial}, Suma: {suma}")
        
        
        if diferencia < 0.0001:
            break
        
        n += 1

    return suma


resultado = calcular_euler()
print(f"\nValor aproximado de e: {resultado}")