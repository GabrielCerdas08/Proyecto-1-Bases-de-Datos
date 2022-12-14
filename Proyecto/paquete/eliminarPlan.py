import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox, ttk
from unittest import result
from webbrowser import get
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
def ventanaEliminarCursoPlan():
    ventanaEliminarCursoPlan= tk.Toplevel()
    ventanaEliminarCursoPlan.title ("Eliminar relacion de cursos y plan de estudio")
    ventanaEliminarCursoPlan.config (width=400, height=400)
    ventanaEliminarCursoPlan.resizable(False, False)

    def volverMenu():
        ventanaEliminarCursoPlan.withdraw()

    label5 = Label (ventanaEliminarCursoPlan, text= "Eliminar relacion de cursos y plan de estudio")
    label5.place(x=10, y=10)
    label5.config(font=("Verdana", 12, BOLD))

    label6 = Label (ventanaEliminarCursoPlan, text= "Cursos:")
    label6.place(x=20, y=100)
    label6.config(font=("Arial", 12, BOLD))

    combo1 = ttk.Combobox (ventanaEliminarCursoPlan, state="readonly", width=25, values=lista)
    combo1.place(x=90, y=100)

    
    def getCodigo():
        global codigo
        codigo = " "
        nombre = "'"+str(combo1.get())+"'"

        mycursorGetCodigo = conexion.cursor()
        mycursorGetCodigo.execute("SELECT id_curso FROM curso WHERE nombre="+ nombre)
        myresult2 = mycursorGetCodigo.fetchone()
        for x in myresult2:
            codigo = x
        messagebox.showinfo(message="Se ha seleccionado el curso", title= "¡Curso seleccioanado!")
        if codigo == "":
            messagebox.showwarning(message="Debe de llenar todos los espacios", title="Datos incompletos")
        else:
            mycursorBusqueda = conexion.cursor()
            mycursorBusqueda.execute ("SELECT numero_plan FROM intermedia_planestudio_curso WHERE id_curso ="+"'"+codigo+"'")
            listaplanes = [i[0]for i in mycursorBusqueda.fetchall()]
            combo2.configure(values=listaplanes)


    seleccion = Button (ventanaEliminarCursoPlan, text = "Seleccionar",  font=("Arial", 10), width=10, command=getCodigo)
    seleccion.place(x=270, y=95 )

    label6 = Label (ventanaEliminarCursoPlan, text= "Planes asociados:")
    label6.place(x=20, y=150)
    label6.config(font=("Arial", 12, BOLD))

    combo2 = ttk.Combobox (ventanaEliminarCursoPlan, state="readonly", width=25, values=lista)
    combo2.place(x=175, y=150)



    def eliminar():
        planesSTR = combo2.get()
        if codigo == "" or planesSTR == "":
            messagebox.showwarning(message="Debe de llenar todos los espacios", title="Datos incompletos")
            
        else: 
            mycursor= conexion.cursor()
            sql = "DELETE FROM intermedia_planestudio_curso WHERE numero_plan = %s AND id_curso = %s"
            adr = (planesSTR, codigo)

            mycursor.execute(sql, adr)

            conexion.commit()
            messagebox.showinfo(message="Se ha eliminado el curso del plan", title= "¡Curso eliminado!")

    seleccion = Button (ventanaEliminarCursoPlan, text = "Eliminar relacion",  font=("Arial", 10),command=eliminar)
    seleccion.place(x=145, y=200 )

    Volver = Button(ventanaEliminarCursoPlan, text = "Volver",  font=("Arial", 12), width=15, command= volverMenu)
    Volver.place(x=125,y=250)


    
    ventanaEliminarCursoPlan.mainloop()
ventanaEliminarCursoPlan()
