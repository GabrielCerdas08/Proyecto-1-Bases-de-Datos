import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox, ttk

def ventanaEscuela():
    ventanaEscuela = tk.Toplevel()
    ventanaEscuela.title("Registro de Escuela o Área Académica")
    ventanaEscuela.config (width=800, height=450)
    ventanaEscuela.resizable(False, False)

    def volverMenu():
        ventanaEscuela.withdraw()
        import menuPrincipal
        menuPrincipal.ventanaMenu()

    label1 = Label (ventanaEscuela, text= "Registro de Escuela o Área Académica")
    label1.place(x=70, y=50)
    label1.config(font=("Verdana", 24, BOLD))

    label2 = Label (ventanaEscuela, text= "Nombre:")
    label2.place(x=80, y=150)
    label2.config(font=("Arial", 12, BOLD))

    entry1 = ttk.Entry (ventanaEscuela, textvariable="nombreEscuela", font=("Arial", 12), width=20)
    entry1.place(x=250, y=150)

    label3 = Label (ventanaEscuela, text= "Código:")
    label3.place(x=80, y=250)
    label3.config(font=("Arial", 12,BOLD))

    entry2 = ttk.Entry (ventanaEscuela, textvariable="codigoEscuela", font=("Arial", 12), width=20)
    entry2.place(x=250, y=250)

    volverButton = Button(ventanaEscuela, text = "Volver", command=volverMenu,  font=("Arial", 12), width=15)
    volverButton.place(x=600,y=350)

    registrarButton = Button(ventanaEscuela, text = "Registrar",  font=("Arial", 12), width=15)
    registrarButton.place(x=500, y=145)

    limpiarButton = Button(ventanaEscuela, text = "Limpiar Campos",  font=("Arial", 12), width=15)
    limpiarButton.place(x=500, y=245)

    ventanaEscuela.mainloop()

ventanaEscuela()



    
