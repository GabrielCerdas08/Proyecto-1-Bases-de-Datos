import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox, ttk
from unittest import result
import mysql.connector
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
conexion = mysql.connector.connect(user='admin', password='Chester08_',
host = 'proyectobases.cml2o43rn7yp.us-east-1.rds.amazonaws.com', database = 'Proyecto1', port = '3306',  consume_results=True)
lista = []
mycursorBusqueda = conexion.cursor()
mycursorBusqueda.execute ("SELECT nombre FROM curso")
lista = [i[0]for i in mycursorBusqueda.fetchall()]
def ventanaEliminarCurso():
    ventanaEliminarCurso= tk.Toplevel()
    ventanaEliminarCurso.title ("Consultas adicionales")
    ventanaEliminarCurso.config (width=400, height=250)
    ventanaEliminarCurso.resizable(False, False)

    def volverMenu():
        ventanaEliminarCurso.withdraw()
        import menuPrincipal
        menuPrincipal.ventanaMenu()



    label5 = Label (ventanaEliminarCurso, text= "Eliminar cursos")
    label5.place(x=50, y=10)
    label5.config(font=("Verdana", 24, BOLD))

    label6 = Label (ventanaEliminarCurso, text= "Cursos:")
    label6.place(x=20, y=100)
    label6.config(font=("Arial", 12, BOLD))

    
    combo1 = ttk.Combobox (ventanaEliminarCurso, state="readonly", width=25, values=lista)
    combo1.place(x=90, y=100)

    seleccion = Button (ventanaEliminarCurso, text = "Eliminar",  font=("Arial", 10), width=10)
    seleccion.place(x=270, y=95 )

    Volver = Button(ventanaEliminarCurso, text = "Volver",  font=("Arial", 12), width=15, command= volverMenu)
    Volver.place(x=125,y=150)


    
    ventanaEliminarCurso.mainloop()
ventanaEliminarCurso()
