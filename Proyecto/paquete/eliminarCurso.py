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
    ventanaEliminarCurso.title ("Eliminación de Cursos")
    ventanaEliminarCurso.config (width=400, height=250)
    ventanaEliminarCurso.resizable(False, False)

    def volverMenu():
        ventanaEliminarCurso.withdraw()
    
    def getCodigo():
        global codigo  
        codigo = " "
        nombre = "'"+str(combo1.get())+"'"
        mycursorGetCodigo = conexion.cursor()
        mycursorGetCodigo.execute("SELECT id_curso FROM curso WHERE nombre="+nombre)
        myresult = mycursorGetCodigo.fetchone()
        for x in myresult:
            codigo = x 
        if codigo == "":
            messagebox.showwarning(message="Debe de llenar todos los espacios", title="Datos incompletos")
        mycursorValidacion = conexion.cursor()
        mycursorValidacion.execute("SELECT count(id_curso) FROM intermedia_planestudio_curso WHERE id_curso ="+"'"+codigo+"'")
        lista = mycursorValidacion.fetchone()
        cantidadVeces = lista[0]
        if(cantidadVeces >= 1):
            messagebox.showwarning(message="No es posible eliminar un curso asignado a un plan de estudios", title="Solicitud inválida")
        else:
            mycursor = conexion.cursor()
            sql = ("DELETE FROM curso WHERE id_curso ="+"'"+codigo+"'")
            mycursor.execute(sql)
            conexion.commit()
            messagebox.showinfo(message="Se ha eliminado el curso del plan", title= "¡Curso eliminado!")
         

    label5 = Label (ventanaEliminarCurso, text= "Eliminar cursos")
    label5.place(x=50, y=10)
    label5.config(font=("Verdana", 24, BOLD))

    label6 = Label (ventanaEliminarCurso, text= "Cursos:")
    label6.place(x=20, y=100)
    label6.config(font=("Arial", 12, BOLD))

    
    combo1 = ttk.Combobox (ventanaEliminarCurso, state="readonly", width=25, values=lista)
    combo1.place(x=90, y=100)

    seleccion = Button (ventanaEliminarCurso, text = "Eliminar",  font=("Arial", 10), width=10, command=getCodigo)
    seleccion.place(x=270, y=95 )

    Volver = Button(ventanaEliminarCurso, text = "Volver",  font=("Arial", 12), width=15, command= volverMenu)
    Volver.place(x=125,y=150)


    
    ventanaEliminarCurso.mainloop()
ventanaEliminarCurso()
