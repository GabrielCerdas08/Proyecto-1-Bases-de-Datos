import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox, ttk

def ventanaRequisitos():
    ventanaRequisitos = Toplevel()
    ventanaRequisitos.title("Asignar requistos y correquistos a un curso")
    ventanaRequisitos.config (width=800, height=550)
    ventanaRequisitos.resizable(False, False)

    def volverMenu():
        ventanaRequisitos.withdraw()
        import menuPrincipal
        menuPrincipal.ventanaMenu()

    label1 = Label (ventanaRequisitos, text= "Asignar requistos y correquistos a un curso")
    label1.place(x=75, y=50)
    label1.config(font=("Verdana", 20, BOLD))

    label2 = Label (ventanaRequisitos, text= "Escuela propetaria del curso:")
    label2.place(x=80, y=150)
    label2.config(font=("Arial", 12, BOLD))

    combo1 = ttk.Combobox (ventanaRequisitos, state="readonly", width=50 )
    combo1.place(x=350, y=150)

    label3 = Label (ventanaRequisitos, text= "Código del curso:")
    label3.place(x=80, y=250)
    label3.config(font=("Arial", 12, BOLD))

    combo2 = ttk.Combobox (ventanaRequisitos, state="readonly", width=10 )
    combo2.place(x=350, y=250)

    label4= Label (ventanaRequisitos, text="Requisitos del curso")
    label4.place(x=200, y=350)
    label4.config(font=("Arial", 12, BOLD))

    label5= Label (ventanaRequisitos, text="Correquisitos del curso")
    label5.place(x=450, y=350)
    label5.config(font=("Arial", 12, BOLD))

    label6= Label (ventanaRequisitos, text="Código del curso:")
    label6.place(x=200, y=380)
    label6.config(font=("Arial", 10, BOLD))

    label7= Label (ventanaRequisitos, text="Código del curso:")
    label7.place(x=450, y=380)
    label7.config(font=("Arial", 10, BOLD))

    combo3 = ttk.Combobox (ventanaRequisitos, state="readonly", width=10 )
    combo3.place(x=200, y=410)

    combo4 = ttk.Combobox (ventanaRequisitos, state="readonly", width=10 )
    combo4.place(x=450, y=410)

    volverButton = Button(ventanaRequisitos, text = "Volver", command=volverMenu,  font=("Arial", 12), width=15)
    volverButton.place(x=650,y=500)

    registrarButton = Button(ventanaRequisitos, text = "Registrar Requisito",  font=("Arial", 10), width=15)
    registrarButton.place(x=200, y=450)

    registarButton2 = Button(ventanaRequisitos, text = "Registrar Correquisito",  font=("Arial", 10), width=15)
    registarButton2.place(x=450, y=450)

    ventanaRequisitos.mainloop()

ventanaRequisitos()

