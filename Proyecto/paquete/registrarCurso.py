import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox, ttk

def ventanaCurso():
    ventanaCurso = tk.Toplevel()
    ventanaCurso.title("Registro de Cursos")
    ventanaCurso.config (width=650, height=700)
    ventanaCurso.resizable(False, False)

    def volverMenu():
        ventanaCurso.withdraw()
        import menuPrincipal
        menuPrincipal.ventanaMenu()

    label0 = Label (ventanaCurso, text= "Registro de Cursos")
    label0.place(x=150, y=10)
    label0.config(font=("Verdana", 24, BOLD))

    label1 = Label (ventanaCurso, text= "Escuela del curso:")
    label1.place(x=80, y=70)
    label1.config(font=("Arial", 12, BOLD))

    combo1 = ttk.Combobox (ventanaCurso, state="readonly", width=50 )
    combo1.place(x=250, y=70)

    label2 = Label (ventanaCurso, text= "Nombre del curso:")
    label2.place(x=80, y=150)
    label2.config(font=("Arial", 12, BOLD))

    entry1 = ttk.Entry (ventanaCurso, textvariable="nombreCurso", font=("Arial", 12), width=5)
    entry1.place(x=250, y=150)

    label3 = Label (ventanaCurso, text= "Código del Curso:")
    label3.place(x=80, y=250)
    label3.config(font=("Arial", 12,BOLD))

    label4 = Label (ventanaCurso, text= "xx")
    label4.place(x=250, y=250)
    label4.config(font=("Arial", 12))

    entry2 = ttk.Entry (ventanaCurso, textvariable="codigoCurso", font=("Arial", 12), width=5)
    entry2.place(x=275, y=250)

    label5 = Label (ventanaCurso, text= "Creditos:")
    label5.place(x=80, y=350)
    label5.config(font=("Arial", 12,BOLD))

    combo2 = ttk.Combobox (ventanaCurso, state="readonly", width=5 )
    combo2.place(x=250, y=350)

    label6 = Label (ventanaCurso, text= "Horas lectivas:")
    label6.place(x=80, y=450)
    label6.config(font=("Arial", 12,BOLD))

    combo3 = ttk.Combobox (ventanaCurso, state="readonly", width=5 )
    combo3.place(x=250, y=450)

    volverButton = Button(ventanaCurso, text = "Volver", command=volverMenu,  font=("Arial", 12), width=15)
    volverButton.place(x=500,y=650)

    registrarButton = Button(ventanaCurso, text = "Registrar",  font=("Arial", 12), width=15)
    registrarButton.place(x=150, y=550)

    limpiarButton = Button(ventanaCurso, text = "Limpiar Campos",  font=("Arial", 12), width=15)
    limpiarButton.place(x=350, y=550)

    ventanaCurso.mainloop()

ventanaCurso()

