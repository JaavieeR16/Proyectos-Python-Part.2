'''
Crea un programa que permite al usuario almacenar, buscar y eliminar contactos en una agenda, utilizando un archivo para guardar la información.
'''

import os

archivo_agenda = "agenda.txt"

def cargar_contactos():
    contactos = {}
    if os.path.exists(archivo_agenda):
        with open(archivo_agenda, "r") as archivo:
            for linea in archivo:
                nombre, telefono = linea.strip().split(",")
                contactos[nombre] = telefono
    return contactos

# Función para guardar los contactos en el archivo
def guardar_contactos(contactos):
    with open(archivo_agenda, "w") as archivo:
        for nombre, telefono in contactos.items():
            archivo.write(f"{nombre},{telefono}\n")

# Función para agregar un nuevo contacto
def agregar_contacto(contactos):
    nombre = input("Introduce el nombre del contacto: ").strip()
    if nombre in contactos:
        print("El contacto ya existe.")
    else:
        telefono = input("Introduce el teléfono del contacto: ").strip()
        contactos[nombre] = telefono
        guardar_contactos(contactos)
        print(f"Contacto {nombre} agregado correctamente.")

def buscar_contacto(contactos):
    nombre = input("Introduce el nombre del contacto que deseas buscar: ").strip()
    if nombre in contactos:
        print(f"Contacto encontrado: {nombre} - Teléfono: {contactos[nombre]}")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto(contactos):
    nombre = input("Introduce el nombre del contacto que deseas eliminar: ").strip()
    if nombre in contactos:
        del contactos[nombre]
        guardar_contactos(contactos)
        print(f"Contacto {nombre} eliminado correctamente.")
    else:
        print("Contacto no encontrado.")

def agenda():
    contactos = cargar_contactos()
    
    while True:
        print("\n--- Agenda de Contactos ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Salir")
        
        opcion = input("Elige una opción: ").strip()
        
        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            buscar_contacto(contactos)
        elif opcion == "3":
            eliminar_contacto(contactos)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    agenda()
