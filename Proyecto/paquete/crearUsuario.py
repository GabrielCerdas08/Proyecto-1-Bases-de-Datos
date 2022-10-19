from optparse import Values
import tkinter as tk
from tkinter import *
import tkinter
from tkinter.font import BOLD
from tkinter import messagebox, ttk
from unittest import result
import mysql.connector

conexion = mysql.connector.connect(user='admin', password='Chester08_',
host = 'proyectobases.cml2o43rn7yp.us-east-1.rds.amazonaws.com', database = 'Proyecto1', port = '3306',  consume_results=True)



def ventanaRegistro():
    ventanaRegistro= tk.Tk()
    ventanaRegistro.title ("Registro de usuarios")
    ventanaRegistro.config (width=400, height=400)
    ventanaRegistro.resizable(False, False)

    label1 = Label (ventanaRegistro, text= "Registro de usuarios")
    label1.place(x=20, y=10)
    label1.config(font=("Verdana", 24, BOLD))

    
    label2 = Label (ventanaRegistro, text= "Identificacion:  ")
    label2.place(x=20, y=100)
    label2.config(font=("Arial", 12, BOLD))

    validate_entry = lambda text: text.isdecimal()
    id = ttk.Entry (ventanaRegistro, textvariable="id", font=("Arial", 12), width=20)
    id.place(x=200, y=100)

    label4 = Label (ventanaRegistro, text= "Nombre completo:  ")
    label4.place(x=20, y=150)
    label4.config(font=("Arial", 12, BOLD))

    nombre = ttk.Entry (ventanaRegistro, textvariable="nombre", font=("Arial", 12), width=20)
    nombre.place(x=200, y=150)

    label3 = Label (ventanaRegistro, text= "Contraseña:  ")
    label3.place(x=20, y=200)
    label3.config(font=("Arial", 12, BOLD))

    contrasenia = ttk.Entry (ventanaRegistro, textvariable="contrasenia", font=("Arial", 12), width=20, show='*')
    contrasenia.place(x=200, y=200)

    label5 = Label (ventanaRegistro, text= "Rol:  ")
    label5.place(x=20, y=250)
    label5.config(font=("Arial", 12, BOLD))

    combo3 = ttk.Combobox (ventanaRegistro, state="readonly", width=15, values= ('Usuario', 'Administrador')) 
    combo3.place(x=200, y=250)


    def volver():
        ventanaRegistro.withdraw()

        
    def insert():
        idSTR = id.get()
        nombreSTR = nombre.get()
        contraseniaSTR = contrasenia.get()
        rolSTR = combo3.get()

        if idSTR == "" or nombreSTR == "" or contraseniaSTR == "" or rolSTR == "":
            messagebox.showwarning(message="Por favor rellene los campos", title="Datos incompletos")
        else:
            mycursor = conexion.cursor()
            sql = "INSERT INTO usuario (nombre_Usuario, password, rol, id) VALUES (%s, %s, %s, %s)"
            val = (nombreSTR, contraseniaSTR,rolSTR, idSTR)
            mycursor.execute(sql, val)
            conexion.commit()
            messagebox.showinfo(message="Persona registrada a nombre de: "+nombreSTR, title="Registro completo")
            volver()

    crearButton = Button(ventanaRegistro, text = "Registrar", command=insert,   font=("Arial", 12), width=15)
    crearButton.place(x=125,y=300)



    volverButton = Button(ventanaRegistro, text = "Volver", command= volver,  font=("Arial", 12), width=15)
    volverButton.place(x=125,y=350)


    ventanaRegistro.mainloop()

ventanaRegistro()