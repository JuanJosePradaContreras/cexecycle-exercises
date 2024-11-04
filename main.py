#Ejercicio 7, parte 2

#Programa para dibujar un triangulo




def dibujar_triangulo(altura):
    for i in range(1, altura + 1):
        print('*' * i)

# Solicitar altura al usuario
altura = int(input("Altura: "))
dibujar_triangulo(altura)