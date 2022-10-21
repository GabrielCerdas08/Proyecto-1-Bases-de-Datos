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
def ventanaEliminarCursoReque():
    ventanaEliminarCursoReque= tk.Toplevel()
    ventanaEliminarCursoReque.title ("Eliminar relacion de cursos y requistos")
    ventanaEliminarCursoReque.config (width=400, height=400)
    ventanaEliminarCursoReque.resizable(False, False)

    def volverMenu():
        ventanaEliminarCursoReque.withdraw()


    def getCodigo():
        global codigo
        codigo = " "
        nombre = "'"+str(combo2.get())+"'"

        mycursorGetCodigo = conexion.cursor()
        mycursorGetCodigo.execute("SELECT id_curso FROM curso WHERE nombre="+ nombre)
        myresult = mycursorGetCodigo.fetchone()
        for x in myresult:
            codigo = x
        messagebox.showinfo(message="Se ha seleccionado el curso", title="¡Curso seleccionado!")
        if codigo == "":
            messagebox.showwarning(message="Debe llenar todos los espacios")
        else:
            mycursorBusqueda = conexion.cursor()
            mycursorBusqueda.execute ("SELECT id_curso_requisito FROM requisitos WHERE id_curso_original ="+"'"+codigo+"'")
            listaRequisitos = [i[0] for i in mycursorBusqueda.fetchall()]
            combo2.configure(values=listaRequisitos)


    label5 = Label (ventanaEliminarCursoReque, text= "Eliminar relacion de cursos y requisitos")
    label5.place(x=10, y=10)
    label5.config(font=("Verdana", 12, BOLD))

    label6 = Label (ventanaEliminarCursoReque, text= "Cursos:")
    label6.place(x=20, y=100)
    label6.config(font=("Arial", 12, BOLD))

    combo1 = ttk.Combobox (ventanaEliminarCursoReque, state="readonly", width=25, values=lista)
    combo1.place(x=90, y=100)

    seleccion = Button (ventanaEliminarCursoReque, text = "Seleccionar",  font=("Arial", 10), width=10,command=getCodigo)
    seleccion.place(x=270, y=95 )

    label6 = Label (ventanaEliminarCursoReque, text= "Requisitos asociados:")
    label6.place(x=20, y=150)
    label6.config(font=("Arial", 12, BOLD))

    combo2 = ttk.Combobox (ventanaEliminarCursoReque, state="readonly", width=25, values=lista)
    combo2.place(x=200, y=150)

    def eliminar():
        requisitosSTR = combo2.get()
        if codigo == "" or requisitosSTR == "":
            messagebox.showwarning(message="Debe de llenar todos los espacios", title="Datos incompletos")
        else:
            mycursor = conexion.cursor()
            sql = "DELETE FROM requisitos WHERE id_curso_original = %s AND id_curso_requisito = %s"
            adr = (requisitosSTR, codigo)

            mycursor.execute(sql, adr)

            conexion.commit()

            messagebox.showinfo(message="Se ha eliminado el requisito del curso", title= "¡Curso eliminado!")

    seleccion = Button (ventanaEliminarCursoReque, text = "Eliminar relacion",  font=("Arial", 10), command=eliminar)
    seleccion.place(x=145, y=200 )

    Volver = Button(ventanaEliminarCursoReque, text = "Volver",  font=("Arial", 12), width=15, command=volverMenu)
    Volver.place(x=125,y=250)


    
    ventanaEliminarCursoReque.mainloop()
ventanaEliminarCursoReque()
