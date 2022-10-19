import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox, ttk

import mysql.connector

conexion = mysql.connector.connect(user='admin', password='Chester08_',
host = 'proyectobases.cml2o43rn7yp.us-east-1.rds.amazonaws.com', database = 'Proyecto1', port = '3306', consume_results=True)



def ventanaEscuela():
    ventanaEscuela = tk.Toplevel()
    ventanaEscuela.title("Registro de Escuela o Área Académica")
    ventanaEscuela.config (width=800, height=450)
    ventanaEscuela.resizable(False, False)

    def volverMenu():
        ventanaEscuela.withdraw()


    label1 = Label (ventanaEscuela, text= "Registro de Escuela o Área Académica")
    label1.place(x=70, y=50)
    label1.config(font=("Verdana", 24, BOLD))

    label2 = Label (ventanaEscuela, text= "Nombre:")
    label2.place(x=80, y=150)
    label2.config(font=("Arial", 12, BOLD))

    nombreEscuela = ttk.Entry (ventanaEscuela, textvariable="nombreEscuela", font=("Arial", 12), width=20)
    nombreEscuela.place(x=250, y=150)

        

    label3 = Label (ventanaEscuela, text= "Código:")
    label3.place(x=80, y=250)
    label3.config(font=("Arial", 12,BOLD))

    codigoEscuela = ttk.Entry (ventanaEscuela, textvariable="codigoEscuela", font=("Arial", 12), width=20)
    codigoEscuela.place(x=250, y=250)

    


    def insert():
        nombreEscuelaSTR = nombreEscuela.get()
        codigoEscuelaSTR = codigoEscuela.get()
        if codigoEscuelaSTR == "" or nombreEscuelaSTR == "":
            messagebox.showwarning(message="Por favor rellene los campos", title="Datos incompletos")
        else:
            mycursor = conexion.cursor()
            sql = "INSERT INTO area_academica (codigo_area_academica, nombre) VALUES (%s, %s)"
            val = (codigoEscuelaSTR, nombreEscuelaSTR)
            mycursor.execute(sql, val)
            conexion.commit()
            messagebox.showinfo(message="Escuela o area academica registrada", title="Registro completo")

    def limpiar():
        nombreEscuela.delete(0,END)
        codigoEscuela.delete(0,END)

    volverButton = Button(ventanaEscuela, text = "Volver", command=volverMenu,  font=("Arial", 12), width=15)
    volverButton.place(x=600,y=350)

    registrarButton = Button(ventanaEscuela, text = "Registrar",  font=("Arial", 12), width=15, command= insert)
    registrarButton.place(x=500, y=145)

    limpiarButton = Button(ventanaEscuela, text = "Limpiar Campos",  font=("Arial", 12), width=15, command=limpiar)
    limpiarButton.place(x=500, y=245)

    ventanaEscuela.mainloop()

ventanaEscuela()



    
