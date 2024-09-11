'''
Crea un programa que muestra la hora actual en formato digital y se actualiza en tiempo.
'''

import tkinter as tk
from time import strftime

def actualizar_hora():
    hora_actual = strftime('%H:%M:%S')
    etiqueta_hora.config(text=hora_actual)
    etiqueta_hora.after(1000, actualizar_hora)

ventana = tk.Tk()
ventana.title("Reloj Digital")
ventana.geometry("250x100")
ventana.resizable(False, False)

etiqueta_hora = tk.Label(ventana, font=('calibri', 40, 'bold'), background='blue', foreground='white')
etiqueta_hora.pack(anchor='center')

actualizar_hora()

ventana.mainloop()
