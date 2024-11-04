#Ejercicio 7, parte 1

#Programa para dibujar un rectángulo




def dibujar_rectangulo(altura, ancho):
    for _ in range(altura):
        print('*' * ancho)

altura = int(input("Altura: "))
ancho = int(input("Ancho: "))
dibujar_rectangulo(altura, ancho)