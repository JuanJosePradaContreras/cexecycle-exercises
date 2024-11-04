#Ejercicio 5

#Escriba un programa que entregue todos los divisores del número entero ingresado:

#Ingrese numero: 200
#1 2 4 5 8 10 20 25 40 50 100 200





def mostrar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores


numero = int(input("Ingrese número: "))
divisores = mostrar_divisores(numero)


print(" ".join(map(str, divisores)))