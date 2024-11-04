#Ejercicio 8

#Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:

#π=4(1−13+15−17+…)
#La entrada del programa debe ser un número entero n
# que indique cuántos términos de la suma se utilizará.
#
#n: 3
#3.466666666666667
#n: 1000
#3.140592653839794


def estimar_pi(n):
    suma = 0
    for k in range(n):
        # Calcula cada término de la serie
        termino = ((-1) ** k) / (2 * k + 1)
        suma += termino
    return 4 * suma

# Solicitar al usuario que ingrese el número de términos
n = int(input("n: "))
valor_pi = estimar_pi(n)

# Imprimir el resultado
print(valor_pi)