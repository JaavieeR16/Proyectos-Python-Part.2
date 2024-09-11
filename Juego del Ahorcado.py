'''
Implementa el clásico juego del ahorcado, donde el usuario debe adivinar una palabra letra por letra antes de quedarse sin intentos.
'''

import random

palabras = ["python", "programacion", "juego", "ahorcado", "desarrollo", "computadora"]

def elegir_palabra():
    return random.choice(palabras)

def jugar_ahorcado():
    palabra = elegir_palabra()
    palabra_oculta = ["_"] * len(palabra)
    intentos_restantes = 6
    letras_adivinadas = []
    
    print("¡Bienvenido al juego del Ahorcado!")
    
    while intentos_restantes > 0 and "_" in palabra_oculta:
        print("\nPalabra:", " ".join(palabra_oculta))
        print(f"Intentos restantes: {intentos_restantes}")
        letra = input("Adivina una letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una letra válida.")
            continue
        
        if letra in letras_adivinadas:
            print(f"Ya adivinaste la letra '{letra}'. Intenta con otra.")
            continue
        
        letras_adivinadas.append(letra)
        
        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_oculta[i] = letra
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
        else:
            intentos_restantes -= 1
            print(f"Lo siento, la letra '{letra}' no está en la palabra.")
    
    if "_" not in palabra_oculta:
        print(f"\n¡Felicidades! Has adivinado la palabra: {palabra}")
    else:
        print(f"\nTe quedaste sin intentos. La palabra era: {palabra}")

if __name__ == "__main__":
    jugar_ahorcado()
