import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox, ttk
import mysql.connector


conexion = mysql.connector.connect(user='admin', password='Chester08_',
host = 'proyectobases.cml2o43rn7yp.us-east-1.rds.amazonaws.com', database = 'Proyecto1', port = '3306',  consume_results=True)
lista = []
mycursorBusqueda = conexion.cursor()
mycursorBusqueda.execute ("SELECT nombre FROM area_academica")
lista = [i[0]for i in mycursorBusqueda.fetchall()]


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
    label2.place(x=50, y=150)
    label2.config(font=("Arial", 12, BOLD))

    combo1 = ttk.Combobox (ventanaPlan, state="readonly", width=50, values=lista)
    combo1.place(x=310, y=150)

    def getCodigo():
        global codigo
        codigo = " "
        nombre = "'"+str(combo1.get())+"'"

        mycursorGetCodigo = conexion.cursor()
        mycursorGetCodigo.execute("SELECT codigo_area_academica FROM area_academica WHERE nombre="+ nombre)
        myresult2 = mycursorGetCodigo.fetchone()
        for x in myresult2:
            codigo = x
            label8.config(text = codigo)
        messagebox.showinfo(message="Se ha seleccionado la escuela", title= "¡Escuela selccionada!")

    seleccion = Button (ventanaPlan, text = "Selecionar", command=getCodigo,  font=("Arial", 10), width=10)
    seleccion.place(x=642 , y=145 )

    label3 = Label (ventanaPlan, text= "Código del plan de Estudios:")
    label3.place(x=80, y=250)
    label3.config(font=("Arial", 12,BOLD))

    label8 = Label (ventanaPlan, text= "")
    label8.place(x=400, y=250)
    label8.config(font=("Arial", 12,BOLD))

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

    values = ['1', '2', '3', '4', '5', '6', '7', '8','9','10','11','12']
    combo2 = ttk.Combobox (ventanaPlan, state="readonly", width=20, values=values )
    combo2.place(x=590, y=500)

    def insert():
        codigoPlanSTR = codigo + entry1.get()
        fechaEntradaVigenciaSTR = entry2.get()
        if codigoPlanSTR == "" or fechaEntradaVigenciaSTR == "":
            messagebox.showwarning(message="Debe de llenar todos los espacios", title="Datos incompletos")
        else:
            mycursor = conexion.cursor()
            sql = "INSERT INTO plan_estudio (numero_plan,fecha_entrada_vigencia,codigo_area_academica)  VALUES (%s, %s, %s)"
            val = (codigoPlanSTR,fechaEntradaVigenciaSTR,codigo)
            mycursor.execute(sql, val)
            conexion.commit()
            messagebox.showinfo(message="Plan de estudio registrado")

    registrarButton = Button(ventanaPlan, text = "Registrar",  font=("Arial", 12), width=15, command=insert)
    registrarButton.place(x=350,y=550)

    volverButton = Button(ventanaPlan, text = "Volver", command=volverMenu,  font=("Arial", 12), width=15)
    volverButton.place(x=600,y=600)
      
    ventanaPlan.mainloop()
ventanaPlan()

          
