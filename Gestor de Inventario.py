'''
Un programa que permite a los usuarios agregar, eliminar y actualizar productos en un inventario. 
Además, puede mostrar la lista de productos disponibles con sus cantidades.
'''

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad):
        if nombre in self.productos:
            self.productos[nombre] += cantidad
            print(f"\n{cantidad} unidades añadidas a {nombre}.")
        else:
            self.productos[nombre] = cantidad
            print(f"\nProducto {nombre} añadido al inventario con {cantidad} unidades.")

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            print(f"\nProducto {nombre} eliminado del inventario.")
        else:
            print(f"\nEl producto {nombre} no existe en el inventario.")

    def actualizar_producto(self, nombre, cantidad):
        if nombre in self.productos:
            self.productos[nombre] = cantidad
            print(f"\nLa cantidad de {nombre} ha sido actualizada a {cantidad} unidades.")
        else:
            print(f"\nEl producto {nombre} no existe en el inventario.")

    def mostrar_inventario(self):
        if self.productos:
            print("\n--- Inventario ---")
            for nombre, cantidad in self.productos.items():
                print(f"{nombre}: {cantidad} unidades")
        else:
            print("\nEl inventario está vacío.")

def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú del Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            nombre = input("Introduce el nombre del producto: ").strip()
            cantidad = int(input(f"Introduce la cantidad de {nombre}: ").strip())
            inventario.agregar_producto(nombre, cantidad)
        elif opcion == "2":
            nombre = input("Introduce el nombre del producto a eliminar: ").strip()
            inventario.eliminar_producto(nombre)
        elif opcion == "3":
            nombre = input("Introduce el nombre del producto a actualizar: ").strip()
            cantidad = int(input(f"Introduce la nueva cantidad de {nombre}: ").strip())
            inventario.actualizar_producto(nombre, cantidad)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            print("Saliendo... Gracias por usar el sistema de inventario.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
