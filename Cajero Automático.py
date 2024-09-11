'''
Un programa que simula las operaciones básicas de un cajero automático, como consultar saldo, retirar dinero, y hacer depósitos.
'''

class CajeroAutomatico:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def consultar_saldo(self):
        print(f"\nSaldo actual: ${self.saldo:.2f}")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"\nHas depositado: ${cantidad:.2f}. Saldo actualizado: ${self.saldo:.2f}")
        else:
            print("\nLa cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("\nFondos insuficientes. No puedes retirar más de lo que tienes en tu cuenta.")
        elif cantidad <= 0:
            print("\nLa cantidad a retirar debe ser mayor que 0.")
        else:
            self.saldo -= cantidad
            print(f"\nHas retirado: ${cantidad:.2f}. Saldo actualizado: ${self.saldo:.2f}")

def menu():
    cajero = CajeroAutomatico(saldo_inicial=1000)  

    while True:
        print("\n--- Menú del Cajero Automático ---")
        print("1. Consultar saldo")
        print("2. Hacer un depósito")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            cajero.consultar_saldo()
        elif opcion == "2":
            cantidad = float(input("Introduce la cantidad a depositar: ").strip())
            cajero.depositar(cantidad)
        elif opcion == "3":
            cantidad = float(input("Introduce la cantidad a retirar: ").strip())
            cajero.retirar(cantidad)
        elif opcion == "4":
            print("Saliendo... Gracias por usar el cajero.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
