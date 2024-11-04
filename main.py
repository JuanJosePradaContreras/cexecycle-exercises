#Ejercicio 2

#Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la 
#ingresada por el usuario:


def potencias_de_dos(n):
    for i in range(n + 1):
        print(f"2^{i} = {2 ** i}")

def main():
    # Solicitar la entrada al usuario
    n = int(input("Ingrese el valor de n (potencia máxima): "))
    
    # Generar y mostrar las potencias de 2
    potencias_de_dos(n)

# Llama a la función principal
main()