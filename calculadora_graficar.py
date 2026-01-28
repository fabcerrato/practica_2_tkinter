def calculadora_graficar():
    #ventana_secundaria = tk.Toplevel(root)
    #ventana_secundaria.title("Calculadora Científica")
    #ventana_secundaria.geometry("300x300")
    from tkinter import messagebox
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    class GraficadorArbolesSimple:
        def __init__(self, root):
            self.root = root
            self.root.title("Graficador Simple")
            self.root.geometry("600x500")

            # Especies de árboles
            self.especies = ["Caoba", "Roble", "Cedro Real"]
            self.datos = {especie: "" for especie in self.especies}

            self.crear_interfaz()

        def crear_interfaz(self):
            # Título
            titulo = tk.Label(self.root, text="Ingresa los Datos",
                              font=("Arial", 14, "bold"))
            titulo.pack(pady=10)

            # Frame para entradas
            frame_entradas = tk.Frame(self.root)
            frame_entradas.pack(pady=10)

            # Crear entradas para cada especie
            self.entries = {}
            for i, especie in enumerate(self.especies):
                # Etiqueta
                label = tk.Label(frame_entradas, text=f"{especie} (metros):", width=15, anchor="w")
                label.grid(row=i, column=0, padx=5, pady=5)

                # Campo de entrada
                entry = tk.Entry(frame_entradas, width=10)
                entry.grid(row=i, column=1, padx=5, pady=5)
                self.entries[especie] = entry

            # Frame para botones
            frame_botones = tk.Frame(self.root)
            frame_botones.pack(pady=20)

            # Botones
            btn_graficar = tk.Button(frame_botones, text="Generar Gráfica",
                                     command=self.generar_grafica, bg="#4CAF50", fg="white")
            btn_graficar.pack(side=tk.LEFT, padx=5)

            btn_limpiar = tk.Button(frame_botones, text="Limpiar Datos",
                                    command=self.limpiar_datos, bg="#f44336", fg="white")
            btn_limpiar.pack(side=tk.LEFT, padx=5)

            # Frame para la gráfica
            self.frame_grafica = tk.Frame(self.root)
            self.frame_grafica.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        def generar_grafica(self):
            # Obtener y validar datos
            alturas = []
            especies_validas = []

            for especie in self.especies:
                valor = self.entries[especie].get().strip()
                if valor:
                    try:
                        altura = float(valor)
                        if altura > 0:
                            alturas.append(altura)
                            especies_validas.append(especie)
                        else:
                            messagebox.showerror("Error", f"La altura de {especie} debe ser positiva")
                            return
                    except ValueError:
                        messagebox.showerror("Error", f"Valor inválido para {especie}")
                        return
                else:
                    messagebox.showerror("Error", f"Ingresa la altura para {especie}")
                    return

            # Limpiar gráfica anterior
            for widget in self.frame_grafica.winfo_children():
                widget.destroy()

            # Crear gráfica
            fig, ax = plt.subplots(figsize=(6, 4))

            # Colores para las barras
            colores = ['#8B4513', '#CD853F', '#D2691E']  # Marrones y tonos madera

            # Crear gráfica de barras
            barras = ax.bar(especies_validas, alturas, color=colores, alpha=0.7)

            # Personalizar gráfica
            ax.set_title('Alturas de Árboles Maderables', fontweight='bold')
            ax.set_ylabel('Altura (metros)')
            ax.set_xlabel('Especies')

            # Añadir valores en las barras
            for barra, altura in zip(barras, alturas):
                ax.text(barra.get_x() + barra.get_width() / 2, barra.get_height() + 0.1,
                        f'{altura}m', ha='center', va='bottom', fontweight='bold')

            # Ajustar límites del eje Y
            ax.set_ylim(0, max(alturas) * 1.2)

            # Mostrar gráfica en la interfaz
            canvas = FigureCanvasTkAgg(fig, master=self.frame_grafica)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        def limpiar_datos(self):
            # Limpiar todos los campos de entrada
            for entry in self.entries.values():
                entry.delete(0, tk.END)

            # Limpiar gráfica
            for widget in self.frame_grafica.winfo_children():
                widget.destroy()

    def main():
        root = tk.Tk()
        app = GraficadorArbolesSimple(root)
        root.mainloop()

    if __name__ == "__main__":
        main()
