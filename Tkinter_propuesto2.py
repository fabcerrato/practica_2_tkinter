# Realizar un programa a modo Ventana, que posea un menú de opciones
# (Editar en la cual se pueda escribir un texto y guardarlos en la pc, modificar la información en bloc de notas, que recupere el archivo. Una opción que ingrese por
# teclado los valores para que calculadora realice
# ( a demás de las operaciones básicas (sumar, restar, multiplicar, dividir ) , pueda calcular y  graficar (fijas o Animadas),   una función lineal  y
# del seno, así como la tangente. Otra opción de menú, que ingrese por teclado el número de personas que participan en la encuesta,
# para ingresar las preferencia o votación de  4 deportes, seleccionados por radio button  cada  y que  muestre un gráficos de  barras de  las cantidades
# de personas que juegan cada deporte. Y una opción salir del programa. Cada opción de menú debe tener su botón  cerrar.

import tkinter as tk
from tkinter import *

root = Tk()


#Configuraciones de la ventana principal

root.title("Practica 2 TKINTER")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg="lightblue")




menubar = Menu(root)
root.config(menu=menubar)

fileditor = Menu(menubar, tearoff=0)
fileditor.add_command(label="Nuevo", command=lambda: abrir_editor())
fileditor.add_command(label="Abrir")
fileditor.add_command(label="Guardar")


editcalc = Menu(menubar, tearoff=0)
editcalc.add_command(label="Estandar", command=lambda: calculadora_estandar())
editcalc.add_command(label="Científica", command=lambda: calculadora_cientifica())
editcalc.add_command(label="Graficos", command=lambda: graficos())

encuesta = Menu(menubar, tearoff=0)
encuesta.add_command(label="Agregar", command=lambda: encuesta())

salir = Menu(menubar, tearoff=0)


menubar.add_cascade(label="Editor de archivo", menu=fileditor)
menubar.add_cascade(label="Calculadora", menu=editcalc)
menubar.add_cascade(label="Encuesta", menu=encuesta)
menubar.add_cascade(label="Salir", menu=salir)


def abrir_editor():
    ventana_secundaria = tk.Toplevel(root)
    ventana_secundaria.title("Editor de archivo")
    ventana_secundaria.geometry("300x300")

def calculadora_estandar():
    ventana_secundaria = tk.Toplevel(root)
    ventana_secundaria.title("Calculadora Estandar")
    ventana_secundaria.geometry("300x300")

def calculadora_cientifica():
    ventana_secundaria = tk.Toplevel(root)
    ventana_secundaria.title("Calculadora Científica")
    ventana_secundaria.geometry("300x300")

def graficos():
    ventana_secundaria = tk.Toplevel(root)
    ventana_secundaria.title("Graficos")
    ventana_secundaria.geometry("300x300")

def encuesta():
    ventana_secundaria = tk.Toplevel(root)
    ventana_secundaria.title("Encuesta")
    ventana_secundaria.geometry("300x300")













# Finalmente bucle de la aplicación
root.mainloop()
