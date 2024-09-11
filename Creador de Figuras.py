'''
Un programa que dibuja figuras simples como triángulos, cuadrados y pirámides usando asteriscos según la altura o el 
tamaño que el usuario indique.
'''

def dibujar_triangulo(altura):
    print("\nTriángulo:")
    for i in range(1, altura + 1):
        print('*' * i)

def dibujar_cuadrado(tamaño):
    print("\nCuadrado:")
    for i in range(tamaño):
        print('*' * tamaño)

def dibujar_piramide(altura):
    print("\nPirámide:")
    for i in range(1, altura + 1):
        espacios = ' ' * (altura - i)
        asteriscos = '*' * (2 * i - 1)
        print(espacios + asteriscos)

def menu():
    while True:
        print("\n--- Menú de Figuras ---")
        print("1. Dibujar Triángulo")
        print("2. Dibujar Cuadrado")
        print("3. Dibujar Pirámide")
        print("4. Salir")
        
        opcion = input("Elige una opción: ").strip()
        
        if opcion == "1":
            altura = int(input("Introduce la altura del triángulo: ").strip())
            dibujar_triangulo(altura)
        elif opcion == "2":
            tamaño = int(input("Introduce el tamaño del cuadrado: ").strip())
            dibujar_cuadrado(tamaño)
        elif opcion == "3":
            altura = int(input("Introduce la altura de la pirámide: ").strip())
            dibujar_piramide(altura)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
