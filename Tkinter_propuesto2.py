# Realizar un programa a modo Ventana, que posea un menú de opciones:
# 1) EDITOR DE TEXTO: Editar en la cual se pueda escribir un texto y guardarlos en la pc, modificar la información en bloc de notas, que recupere el archivo.
# 2) CALCULADORA ESTÁNDAR: Una opción que ingrese por teclado los valores para que calculadora realice  a demás de las operaciones básicas (sumar, restar, multiplicar, dividir,
# 3) CALCULADORA CIENTÍFICA: pueda calcular y  graficar (fijas o Animadas),
# 4) GRAFICOS: una función lineal y del seno, así como la tangente.
# 5) ENCUESTA: Otra opción de menú, que ingrese por teclado el número de personas que participan en la encuesta, para ingresar las preferencia o votación de  4 deportes,
# seleccionados por radio button  cada  y que  muestre un gráficos de  barras de  las cantidades de personas que juegan cada deporte.
# 6) SALIR: Y una opción salir del programa. Cada opción de menú debe tener su botón  cerrar.

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math


root = Tk()

#Configuraciones de la ventana principal
root.title("Practica 2 TKINTER")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg="lightblue")

# variables globales
cantidad_personas = 0
contador_personas = 0
Baloncesto = 0
Boleybol = 0
Beisbol = 0
Futbol = 0


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
    ventana_secundaria.geometry("800x700")

    # Crear figura de matplotlib
    fig, ax = plt.subplots(figsize=(8, 5))
    canvas = FigureCanvasTkAgg(fig, master=ventana_secundaria)
    canvas.get_tk_widget().pack()

    frame_datos = tk.Frame(ventana_secundaria)
    frame_datos.pack(pady=10)

    # Etiquetas y cuadros de texto para los parámetros
    et_s = tk.Label(frame_datos, text="Amplitud del Seno:")
    et_s.grid(row=0, column=0, padx=5, pady=5)

    entrada_seno = tk.Entry(frame_datos)
    entrada_seno.insert(0, "1")
    entrada_seno.grid(row=0, column=1, padx=5, pady=5)

    et_fsen = tk.Label(frame_datos, text="Frecuencia del Seno:")
    et_fsen.grid(row=0, column=2, padx=5, pady=5)

    entrada_freq_seno = tk.Entry(frame_datos)
    entrada_freq_seno.insert(0, "1")
    entrada_freq_seno.grid(row=0, column=3, padx=5, pady=5)

    et_lineal = tk.Label(frame_datos, text="Pendiente de la Lineal:")
    et_lineal.grid(row=1, column=0, padx=5, pady=5)

    entrada_lineal = tk.Entry(frame_datos)
    entrada_lineal.insert(0, "0.5")
    entrada_lineal.grid(row=1, column=1, padx=5, pady=5)

    et_ftan = tk.Label(frame_datos, text="Frecuencia de la Tangente:")
    et_ftan.grid(row=2, column=0, padx=5, pady=5)

    entrada_tan = tk.Entry(frame_datos)
    entrada_tan.insert(0, "1")
    entrada_tan.grid(row=2, column=1, padx=5, pady=5) 

    # Función para graficar
    def generar_grafica():
        ax.clear()
        
        # Obtener valores desde la interfaz
        try:
            amp_seno = float(entrada_seno.get())
            freq_seno = float(entrada_freq_seno.get())
            m_lineal = float(entrada_lineal.get())
            freq_tan = float(entrada_tan.get())
        except ValueError:
            ax.text(0.5, 0.5, "Por favor ingrese solo números", ha='center', va='center', transform=ax.transAxes)
            canvas.draw()
            return

        # Rango de valores de x
        x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

        # Calcular funciones
        y_seno = amp_seno * np.sin(freq_seno * x)
        y_tan = np.tan(freq_tan * x)
        y_lineal = m_lineal * x

        # Dibujar las curvas
        ax.plot(x, y_seno, label=f"Seno ({amp_seno}·sin({freq_seno}x))", color='blue')
        ax.plot(x, y_tan, label=f"Tangente ({freq_tan}x)", color='red')
        ax.plot(x, y_lineal, label=f"Lineal ({m_lineal}x)", color='green')

        ax.set_ylim(-10, 10)
        ax.set_title("Gráfica de Seno, Tangente y Función Lineal")
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")
        ax.grid(True)
        ax.legend()

        canvas.draw()

    # Botón para actualizar las gráficas
    boton = tk.Button(ventana_secundaria, text="Graficar", command=generar_grafica)
    boton.pack(pady=10)



def fun_encuesta():
    ventana_secundaria = tk.Toplevel(root)
    ventana_secundaria.title("Encuesta")
    ventana_secundaria.geometry("750x500")


    # Etiqueta de bienvenida
    etiqueta_bienvenida = tk.Label(ventana_secundaria, text="Encuesta de Deportes", font=("Arial", 16, "bold"),
                                   fg="darkblue")
    etiqueta_bienvenida.pack()
    etiqueta_bienvenida2 = tk.Label(ventana_secundaria,
                                    text="La siguiente encuesta tiene por objetivo saber las preferencias del usuario con respecto a 4 deportes",
                                    font=("Arial", 12), fg="black")
    etiqueta_bienvenida2.pack()


    # Pedir la cantidad de encuestados
    et_personas = tk.Label(ventana_secundaria, text="Ingrese el número de encuestados:", font=("Arial", 12))
    et_personas.pack(pady=10)
    entrada_encuestados = tk.Entry(ventana_secundaria, font=("Arial", 12))
    entrada_encuestados.pack(pady=5)

    # Contenedor para los datos de la encuesta
    label_frame = tk.LabelFrame(ventana_secundaria, text="Encuesta", font=("Arial", 12, "bold"), fg="darkblue")

    et = tk.Label(label_frame, text="¿Qué deporte le gusta más?", font=("Arial", 12, "bold"), fg="black")
    et.pack()

    radio_seleccionado = tk.IntVar()

    radio1 = tk.Radiobutton(label_frame, text="Baloncesto", variable=radio_seleccionado, value=1)
    radio2 = tk.Radiobutton(label_frame, text="Boleybol", variable=radio_seleccionado, value=2)
    radio3 = tk.Radiobutton(label_frame, text="Beisbol", variable=radio_seleccionado, value=3)
    radio4 = tk.Radiobutton(label_frame, text="Fútbol", variable=radio_seleccionado, value=4)

    # Mostrar los rb
    radio1.pack(pady=5)
    radio2.pack(pady=5)
    radio3.pack(pady=5)
    radio4.pack(pady=5)


    def limpiar():

        global cantidad_personas, contador_personas, Baloncesto, Boleybol, Beisbol, Futbol
        # Reseteamos variables globales
        cantidad_personas = 0
        contador_personas = 0
        Baloncesto = 0
        Boleybol = 0
        Beisbol = 0
        Futbol = 0

        entrada_encuestados.delete(0, tk.END)  # Limpiamos caja de texto
        radio1.configure(text="Baloncesto")
        radio2.configure(text="Boleybol")
        radio3.configure(text="Beisbol")
        radio4.configure(text="Futbol")

    # Funcion para controlar el siguiente encuestado
    def siguiente():
        global cantidad_personas, contador_personas, Baloncesto, Boleybol, Beisbol, Futbol

        if contador_personas == 1:
            # si es el primero, capturamos lo ingresado en entrada_encuestados
            cantidad_personas = int(entrada_encuestados.get())

        if contador_personas <= cantidad_personas:
            # Actualizamos las variables contadoras
            if radio_seleccionado.get() == 1:
                Baloncesto += 1
                contador_personas += 1
                radio1.configure(text=f"Baloncesto: ({Baloncesto})")
            elif radio_seleccionado.get() == 2:
                Boleybol += 1
                contador_personas += 1
                radio2.configure(text=f"Boleybol: ({Boleybol})")
            elif radio_seleccionado.get() == 3:
                Beisbol += 1
                contador_personas += 1
                radio3.configure(text=f"Beisbol: ({Beisbol})")
            elif radio_seleccionado.get() == 4:
                Futbol += 1
                contador_personas += 1
                radio4.configure(text=f"Futbol: ({Futbol})")
            else:
                messagebox.showerror("Error", "¡Seleccione un deporte!")

        if contador_personas == cantidad_personas:
            #Ya terminó, mostramos el gráfico de barras

            deportes = ['Baloncesto', 'Boleybol', 'Beisbol', 'Fútbol']
            datos = [Baloncesto, Boleybol, Beisbol, Futbol]
            # colores de las barras
            colores = ['#ff9999', '#66B2ff', '#99FF99', '#FFCC66']

            # crea graficos de barras
            plt.bar(deportes, datos, color=colores)

            # Titulo Etiqueta
            plt.title("Preferencias en Deportes")

            # mostar el grafico
            plt.show()


    boton_siguiente = tk.Button(label_frame, text="Siguiente persona", command=lambda: siguiente())
    boton_siguiente.pack(pady=5)

    label_frame.configure(height=200)
    label_frame.pack(pady=10, padx=20, fill="both")

    boton_limpiar = tk.Button(ventana_secundaria, text="Resetear", command=lambda: limpiar())
    boton_limpiar.pack(pady=5)






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
encuesta.add_command(label="Agregar", command=lambda: fun_encuesta())

salir = Menu(menubar, tearoff=0)


menubar.add_cascade(label="Editor de archivo", menu=fileditor)
menubar.add_cascade(label="Calculadora", menu=editcalc)
menubar.add_cascade(label="Encuesta", menu=encuesta)
menubar.add_cascade(label="Salir", menu=salir)




# Finalmente bucle de la aplicación
root.mainloop()

