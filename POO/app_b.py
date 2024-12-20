import random
from laptop_bussiness import Laptop_Bussiness
import tkinter as tk
from tkinter import Image, ttk
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes = ["C:\\Users\\Lesly Villarruel\\Documents\\KRAKEDEV\\MÓDULO 6\\POO\img\\1.jpeg", "C:\\Users\Lesly Villarruel\Documents\KRAKEDEV\\MÓDULO 6\\POO\\img\\2.jpg"]
        root.title("Ingresar Datos")
        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Marca").grid(row=0, column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column=1)
        
        ttk.Label(self.root, text="Procesador").grid(row=1, column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1, column=1)

        ttk.Label(self.root, text="Memoria").grid(row=2, column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2, column=1)

        ttk.Label(self.root, text="Espacio disco").grid(row=3, column=0)
        self.espacio_disco = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.espacio_disco).grid(row=3, column=1)

        ttk.Label(self.root, text="Duracion bateria").grid(row=4, column=0)
        self.duracion_bateria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.duracion_bateria).grid(row=4, column=1)

        ttk.Label(self.root, text="Precio").grid(row=5, column=0)
        self.precio = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.precio).grid(row=5, column=1)

        ttk.Button(self.root, text="Agregar Laptop", command=self.agregar_laptop).grid(row=6, column=0)

        self.canva = tk.Canvas(self.root, width=200, height=200)
        self.canva.grid(row=1, column=3, rowspan=6)

        
        
        self.mostrar_laptops = tk.Text(self.root, height=10, width=50)
        self.mostrar_laptops.grid(row=7, column=0, columnspan=2)

    def agregar_laptop(self):
        nueva_laptop = Laptop_Bussiness(self.marca.get(), self.procesador.get(), self.memoria.get(), self.espacio_disco.get(), self.duracion_bateria.get(), self.precio.get())
        self.laptops.append(nueva_laptop)
        print(self.laptops[0])

        self.mostrar_laptops.insert(tk.END,f"{self.laptops}")
        self.mostrar_imagenes_aleatorias()

    def mostrar_imagenes_aleatorias(self):
        imagen_path = random.choice(self.imagenes)
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((200,200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)

        self.canva.create_image(0,0, anchor=tk.NW, image=photo)
        self.canva.image()

        pass

root = tk.Tk()

app = App(root)
root.mainloop()