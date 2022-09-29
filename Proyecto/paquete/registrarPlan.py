import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox, ttk

def ventanaPlan():
    ventanaPlan= tk.Toplevel()
    ventanaPlan.title ("Crear Plan de Estudios")
    ventanaPlan.config (width=800, height=650)
    ventanaPlan.resizable(False, False)

    def volverMenu():
        ventanaPlan.withdraw()
        import menuPrincipal
        
        menuPrincipal.ventanaMenu()

    label1 = Label (ventanaPlan, text= "Registro de planes de estudio")
    label1.place(x=150, y=50)
    label1.config(font=("Verdana", 24, BOLD))

    label2 = Label (ventanaPlan, text= "Escuela propetaria del curso:")
    label2.place(x=80, y=150)
    label2.config(font=("Arial", 12, BOLD))

    combo1 = ttk.Combobox (ventanaPlan, state="readonly", width=50 )
    combo1.place(x=450, y=150)

    label3 = Label (ventanaPlan, text= "Código del plan de Estudios:")
    label3.place(x=80, y=250)
    label3.config(font=("Arial", 12,BOLD))

    entry1 = ttk.Entry (ventanaPlan, textvariable="codigoPlan", font=("Arial", 12), width=20)
    entry1.place(x=450, y=250)

    label4 = Label (ventanaPlan, text= "Vigencia del plan de estudios:  (DD/MM/YYYY)")
    label4.place(x=80, y=350)
    label4.config(font=("Arial", 12,BOLD))

    entry2 = ttk.Entry (ventanaPlan, textvariable="vigenciaPlan", font=("Arial", 12), width=20)
    entry2.place(x=450, y=350)

    label5 = Label (ventanaPlan, text= "Código del curso que forma parte del plan")
    label5.place(x=100, y=450)
    label5.config(font=("Arial", 12,BOLD))

    entry4 = ttk.Entry (ventanaPlan, textvariable="codigoCursoPlan", font=("Arial", 12), width=20)
    entry4.place(x=150, y=500)

    label6 = Label (ventanaPlan, text= "Bloque")
    label6.place(x=630, y=450)
    label6.config(font=("Arial", 12,BOLD))

    combo2 = ttk.Combobox (ventanaPlan, state="readonly", width=20 )
    combo2.place(x=590, y=500)

    registrarButton = Button(ventanaPlan, text = "Registrar",  font=("Arial", 12), width=15)
    registrarButton.place(x=350,y=550)

    
    
    volverButton = Button(ventanaPlan, text = "Volver", command=volverMenu,  font=("Arial", 12), width=15)
    volverButton.place(x=600,y=600)
      
    ventanaPlan.mainloop()
ventanaPlan()

          
