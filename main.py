#Ejercicio 3

#Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. 
#Por ejemplo, si los números son 1 y 7, #debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.

#Ingrese num: 1
#Ingrese num: 7
#La suma es 20



num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))


if num1 > num2:
    num1, num2 = num2, num1

suma = sum(range(num1 + 1, num2))


print(f"La suma de los números entre {num1} y {num2} es: {suma}")