from operator import imod
from optparse import Values
import tkinter as tk
from tkinter import *
import tkinter
from tkinter.font import BOLD
from tkinter import messagebox, ttk
from unittest import result
import mysql.connector

def ventanaInicio():
    ventanaInicio= tk.Tk()
    ventanaInicio.title ("Inicio de sesión")
    ventanaInicio.config (width=400, height=400)
    ventanaInicio.resizable(False, False)

    label1 = Label (ventanaInicio, text= "Inicio del sistema")
    label1.place(x=40, y=10)
    label1.config(font=("Verdana", 24, BOLD))

    
    label2 = Label (ventanaInicio, text= "Identificacion:  ")
    label2.place(x=20, y=100)
    label2.config(font=("Arial", 12, BOLD))

    id = ttk.Entry (ventanaInicio, textvariable="id", font=("Arial", 12), width=20)
    id.place(x=200, y=100)

    label3 = Label (ventanaInicio, text= "Contraseña:  ")
    label3.place(x=20, y=150)
    label3.config(font=("Arial", 12, BOLD))

    contrasenia = ttk.Entry (ventanaInicio, textvariable="contrasenia", font=("Arial", 12), width=20, show='*')
    contrasenia.place(x=200, y=150)

    def inicio():
        idSTR = "'"+id.get()+"'"
        contraseniaSTR = "'"+contrasenia.get()+"'"
        if idSTR == "" or contraseniaSTR == "":
            messagebox.showwarning(message="Por favor rellene los campos", title="Datos incompletos")
        else:
            rolSTR=""
            conexion = mysql.connector.connect(user='admin', password='Chester08_',
            host = 'proyectobases.cml2o43rn7yp.us-east-1.rds.amazonaws.com', database = 'Proyecto1', port = '3306',  consume_results=True)
            mycursorBusqueda = conexion.cursor()
            mycursorBusqueda.execute ("SELECT rol FROM usuario WHERE id="+idSTR+"AND password="+contraseniaSTR)
            aaa = mycursorBusqueda.fetchone()
            for x in aaa:
                rolSTR = x
                print (rolSTR)


            if rolSTR == 'Administrador':
                ventanaInicio.withdraw()
                import menuPrincipalAdmin
                menuPrincipalAdmin.ventanaMenu()
            if rolSTR == 'Usuario':
                ventanaInicio.withdraw()
                import menuPrincipal
                menuPrincipal.ventanaMenu()
            else:
                messagebox.showwarning(message="Los datos insertados no existen", title="Datos inexistentes")
                id.delete(0,END)
                contrasenia.delete(0, END)



    iniciarButton = Button(ventanaInicio, text = "Iniciar", command= inicio,  font=("Arial", 12), width=15)
    iniciarButton.place(x=125,y=200)

    label4 = Label (ventanaInicio, text= "Si no cuenta con un usuario registrado, \npor favor cree una cuenta")
    label4.place(x=70, y=300)
    label4.config(font=("Arial", 10, BOLD))

    def crear():
        ventanaInicio.withdraw()
        import crearUsuario
        crearUsuario.ventanaRegistro()

    crearButton = Button(ventanaInicio, text = "Registrar",  command=crear, font=("Arial", 12), width=15)
    crearButton.place(x=125,y=350)


    ventanaInicio.mainloop()

ventanaInicio()
