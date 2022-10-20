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
lista = []
mycursorBusqueda = conexion.cursor()
mycursorBusqueda.execute ("SELECT nombre FROM area_academica")
lista = [i[0]for i in mycursorBusqueda.fetchall()]





def ventanaCurso():
    ventanaCurso = tk.Toplevel()
    ventanaCurso.title("Registro de Cursos")
    ventanaCurso.config (width=650, height=700)
    ventanaCurso.resizable(False, False)

    def volverMenu():
        ventanaCurso.withdraw()


    label0 = Label (ventanaCurso, text= "Registro de Cursos")
    label0.place(x=150, y=10)
    label0.config(font=("Verdana", 24, BOLD))

    label1 = Label (ventanaCurso, text= "Escuela del curso:")
    label1.place(x=10, y=70)
    label1.config(font=("Arial", 12, BOLD))

    combo1 = ttk.Combobox (ventanaCurso, state="readonly", width=50, values=lista)
    combo1.place(x=180, y=70)
    

    def getCodigo():
        global codigo
        codigo = " "
        nombre = "'"+str(combo1.get())+"'"

        mycursorGetCodigo = conexion.cursor()
        mycursorGetCodigo.execute("SELECT codigo_area_academica FROM area_academica WHERE nombre="+ nombre)
        myresult2 = mycursorGetCodigo.fetchone()
        for x in myresult2:
            codigo = x
            label4.config(text = codigo)
        messagebox.showinfo(message="Se ha seleccionado la escuela", title= "¡Escuela selccionada!")

        
        

    seleccion = Button (ventanaCurso, text = "Selecionar", command=getCodigo,  font=("Arial", 10), width=10)
    seleccion.place(x=520, y=65 )



    label2 = Label (ventanaCurso, text= "Nombre del curso:")
    label2.place(x=80, y=150)
    label2.config(font=("Arial", 12, BOLD))

    nombreCurso = ttk.Entry (ventanaCurso, textvariable="nombreCurso", font=("Arial", 12), width=5)
    nombreCurso.place(x=250, y=150)

    label3 = Label (ventanaCurso, text= "Código del Curso:")
    label3.place(x=80, y=250)
    label3.config(font=("Arial", 12,BOLD))

    label4 = Label (ventanaCurso, text= "")
    label4.place(x=250, y=250)
    label4.config(font=("Arial", 12))

    codigoCurso = ttk.Entry (ventanaCurso, textvariable="codigoCurso", font=("Arial", 12), width=20)
    codigoCurso.place(x=280, y=250)

    label5 = Label (ventanaCurso, text= "Creditos:")
    label5.place(x=80, y=350)
    label5.config(font=("Arial", 12,BOLD))

    values = ['1', '2', '3', '4', '5', '6', '7', '8']
    combo2 = ttk.Combobox (ventanaCurso, state="readonly", width=5, values= values)
    combo2.place(x=250, y=350)

    label6 = Label (ventanaCurso, text= "Horas lectivas:")
    label6.place(x=80, y=450)
    label6.config(font=("Arial", 12,BOLD))

    combo3 = ttk.Combobox (ventanaCurso, state="readonly", width=5, values= values )
    combo3.place(x=250, y=450)

    def insert():
        nombreCursoSTR = nombreCurso.get()
        codigoCursoSTR = codigo + codigoCurso.get()
        creditosSTR = combo2.get()
        horasSTR = combo3.get()
        if codigo == "" or nombreCursoSTR == "" or codigoCursoSTR == "" or creditosSTR == "" or horasSTR == "":
            messagebox.showwarning(message="Debe de llenar todos los espacios", title="Datos incompletos")
        else:
            mycursor = conexion.cursor()
            sql = "INSERT INTO curso (id_curso,nombre,cantidad_creditos,cantidad_horas_lectivas) VALUES (%s, %s, %s, %s)"
            val = (codigoCursoSTR,nombreCursoSTR,creditosSTR,horasSTR)
            mycursor.execute(sql, val)
            conexion.commit()
            mycursor2 = conexion.cursor()
            sql2 = "INSERT INTO intermedia_escuela_curso (codigo_area_academica,id_curso) VALUES (%s, %s)"
            val2 = (codigo,codigoCursoSTR)
            mycursor.execute(sql2,val2)
            conexion.commit()
            messagebox.showinfo(message="Curso registrado", title="Registro completo")


    def limpiar():
        nombreCurso.delete(0,END)
        codigoCurso.delete(0, END)
        label4.config(text = "")
        combo1.set("")
        combo2.set("")
        combo3.set("")


    volverButton = Button(ventanaCurso, text = "Volver", command=volverMenu,  font=("Arial", 12), width=15)
    volverButton.place(x=500,y=650)

    registrarButton = Button(ventanaCurso, text = "Registrar",  font=("Arial", 12), width=15, command= insert)
    registrarButton.place(x=150, y=550)

    limpiarButton = Button(ventanaCurso, text = "Limpiar Campos",  font=("Arial", 12), width=15, command=limpiar)
    limpiarButton.place(x=350, y=550)

    ventanaCurso.mainloop()

ventanaCurso()

