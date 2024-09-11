'''
Crea un programa para hacer la equivalencia de monedas. 
'''

class ConvertidorMonedas:
    def __init__(self):
        self.tasas_de_cambio = {
            "USD": 0.85,  # Dólar a Euro
            "CNY": 0.13,  # Yuan a Euro
            "MXN": 0.049  # Peso Mexicano a Euro
        }

    def convertir_a_euro(self, moneda_origen, cantidad):
        if moneda_origen in self.tasas_de_cambio:
            tasa = self.tasas_de_cambio[moneda_origen]
            resultado = cantidad * tasa
            print(f"\n{cantidad} {moneda_origen} equivale a {resultado:.2f} EUR")
        else:
            print("\nMoneda no válida o no soportada para la conversión.")

def menu():
    convertidor = ConvertidorMonedas()

    while True:
        print("\n--- Menú del Convertidor de Monedas a Euros ---")
        print("1. Convertir de Dólar (USD) a Euro (EUR)")
        print("2. Convertir de Yuan (CNY) a Euro (EUR)")
        print("3. Convertir de Peso Mexicano (MXN) a Euro (EUR)")
        print("4. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            cantidad = float(input("Introduce la cantidad en Dólares (USD): ").strip())
            convertidor.convertir_a_euro("USD", cantidad)
        elif opcion == "2":
            cantidad = float(input("Introduce la cantidad en Yuanes (CNY): ").strip())
            convertidor.convertir_a_euro("CNY", cantidad)
        elif opcion == "3":
            cantidad = float(input("Introduce la cantidad en Pesos Mexicanos (MXN): ").strip())
            convertidor.convertir_a_euro("MXN", cantidad)
        elif opcion == "4":
            print("Saliendo... Gracias por usar el convertidor.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
