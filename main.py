#Ejercicio 11

#Elabora una secuencia de collatz para numeros enteros



def colltaz_sequence(n):
    secuencia = []
    while n != 1:
        secuencia.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    secuencia.append(1)  
    return secuencia

#
def graficar_longitudes_collatz(max_n):
    print(f"Secuencia de Collatz y sus longitudes hasta {max_n - 1}:")
    for i in range(1, max_n):
        secuencia = colltaz_sequence(i)
        longitud = len(secuencia)
        print(f"{i} {'*' * longitud}")


n = int(input("n: "))
print("\nSecuencia de Collatz:")
print(colltaz_sequence(n))


graficar_longitudes_collatz(n)