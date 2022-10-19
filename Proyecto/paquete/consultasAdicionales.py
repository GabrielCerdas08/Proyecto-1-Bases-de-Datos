

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
def ventanaConsultaAdicional():
    ventanaConsultaAdicional= tk.Toplevel()
    ventanaConsultaAdicional.title ("Consultas adicionales")
    ventanaConsultaAdicional.config (width=500, height=650)
    ventanaConsultaAdicional.resizable(False, False)

    def volverMenu():
        ventanaConsultaAdicional.withdraw()






    label5 = Label (ventanaConsultaAdicional, text= "Consultas adicionales")
    label5.place(x=50, y=10)
    label5.config(font=("Verdana", 24, BOLD))

    label6 = Label (ventanaConsultaAdicional, text= "Cursos:")
    label6.place(x=20, y=100)
    label6.config(font=("Arial", 12, BOLD))

    
    combo1 = ttk.Combobox (ventanaConsultaAdicional, state="readonly", width=25, values=lista)
    combo1.place(x=90, y=100)

    seleccion = Button (ventanaConsultaAdicional, text = "Selecionar",  font=("Arial", 10), width=10)
    seleccion.place(x=270, y=95 )

    label0 = Label (ventanaConsultaAdicional, text= "Planes Asociados:")
    label0.place(x=25, y=175)
    label0.config(font=("Arial", 10, BOLD))
    listPlanes = Listbox(ventanaConsultaAdicional, font=("Arial", 10), width=20)
    listPlanes.place(x=25, y=200)

    label1 = Label (ventanaConsultaAdicional, text= "Requisitos :")
    label1.place(x=175, y=175)
    label1.config(font=("Arial", 10, BOLD))
    listReque = Listbox(ventanaConsultaAdicional, font=("Arial", 10), width=20)
    listReque.place(x=175, y=200)

    label2 = Label (ventanaConsultaAdicional, text= "Correquisitos:")
    label2.place(x=325, y=175)
    label2.config(font=("Arial", 10, BOLD))
    listCorreque = Listbox(ventanaConsultaAdicional, font=("Arial", 10), width=20)
    listCorreque.place(x=325, y=200)

    consultarButton = Button(ventanaConsultaAdicional, text = "Consultar",  font=("Arial", 12), width=15)
    consultarButton.place(x=10,y=450)
    limpiarButton = Button(ventanaConsultaAdicional, text = "Limpiar",  font=("Arial", 12), width=15)
    limpiarButton.place(x=160,y=450)
    Volver = Button(ventanaConsultaAdicional, text = "Volver",  font=("Arial", 12), width=15, command=volverMenu)
    Volver.place(x=310,y=450)



    ventanaConsultaAdicional.mainloop()
ventanaConsultaAdicional()

          