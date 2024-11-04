#Ejercicio 7, parte 3

#Programa para dibujar un hexágono


def dibujar_hexagono(lado):
    
    for i in range(lado):
        print(' ' * (lado - i - 1) + '*' * (2 * i + 2))
    
    
    for i in range(lado - 1):
        print(' ' * (i + 1) + '*' * (2 * (lado - 1 - i) + 2))


lado = int(input("Lado: "))
dibujar_hexagono(lado)