#import la libreria tkinter, con el alias tk
import tkinter as tk
from tkinter import Frame, BOTH, Canvas, PhotoImage, Scale, Label, Button, Entry
from random import randint
# -------------------------------
# VENTANA PRINCIPAL
# -------------------------------
def modificar_arco():
    a = int(blog1.get())
    b = int(blog2.get())
    n = int(blog3.get())
    Lista = [randint(1,9) for i in range(a*b)]
    k = 0
    for i in range(a):
        for j in range(b):
            frame_graficacion = Frame(ventana_principal)
            frame_graficacion.config(bg ="black", width=120, height=120)
            frame_graficacion.place(x=10+130*j, y=50+130*i)
            if Lista[k] == n:
                color = "pink"
            else:
                color = "purple"
            c = Canvas(frame_graficacion, width=100, height=100, bg = color)
            c.place(x=10 , y=10)
            etiqueta = Label(text=str(Lista[k]), font=("Arial", 20, "bold"))
            etiqueta.place(x=60+130*j, y=100+130*i)
            k = k+1

ventana_principal = tk.Tk()
ventana_principal.title("MATRIZ")
ventana_principal.geometry("1000x800")
ventana_principal.resizable(False, False)
etiqueta1 = Label(text="Filas: ", font=("Arial", 10, "bold"))
etiqueta1.place(x=10, y=10)
etiqueta2 = Label(text="Columnas: ", font=("Arial", 10, "bold"))
etiqueta2.place(x=100, y=10)
etiqueta3 = Label(text="N: ", font=("Arial", 10, "bold"))
etiqueta3.place(x=220, y=10)
boton = Button(text="Calcular", command=modificar_arco)
boton.place(x=300, y=10)
blog1 = Entry(text="", width=5)
blog1.place(x=60, y=10)
blog2 = Entry(text="", width=5)
blog2.place(x=180, y=10)
blog3 = Entry(text="", width=5)
blog3.place(x=240, y=10)
#----------------------
# FRAME DE GRAFICACIÓN
#----------------------

# desplegar ventana principal y queda a la espera de lo que el usuario haga 
ventana_principal.mainloop()
