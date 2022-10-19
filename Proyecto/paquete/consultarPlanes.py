
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
mycursorBusqueda.execute ("SELECT nombre FROM area_academica")
lista = [i[0]for i in mycursorBusqueda.fetchall()]


def ventanaConsultaPlan():
    ventanaConsultaPlan= tk.Toplevel()
    ventanaConsultaPlan.title ("Consultar Plan de estudios")
    ventanaConsultaPlan.config (width=800, height=650)
    ventanaConsultaPlan.resizable(False, False)

    lista = ['1','2','3','4']

    
    def volverMenu():
        ventanaConsultaPlan.withdraw()





    label5 = Label (ventanaConsultaPlan, text= "Consultar Plan de estudios")
    label5.place(x=150, y=10)
    label5.config(font=("Verdana", 24, BOLD))

    label6 = Label (ventanaConsultaPlan, text= "Escuela del curso:")
    label6.place(x=10, y=70)
    label6.config(font=("Arial", 12, BOLD))

    
    combo1 = ttk.Combobox (ventanaConsultaPlan, state="readonly", width=25, values=lista)
    combo1.place(x=180, y=70)

    seleccion = Button (ventanaConsultaPlan, text = "Selecionar",  font=("Arial", 10), width=10)
    seleccion.place(x=375, y=65 )

    label7 = Label (ventanaConsultaPlan, text= "Codigo del plan de estudios:")
    label7.place(x=10, y=115)
    label7.config(font=("Arial", 12, BOLD))

    combo2 = ttk.Combobox (ventanaConsultaPlan, state="readonly", width=25, values=lista)
    combo2.place(x=240, y=115)

    seleccion2 = Button (ventanaConsultaPlan, text = "Selecionar",  font=("Arial", 10), width=10)
    seleccion2.place(x=430, y=115 )


    label0 = Label (ventanaConsultaPlan, text= "Codigos:")
    label0.place(x=25, y=175)
    label0.config(font=("Arial", 10, BOLD))
    listCodigos = Listbox(ventanaConsultaPlan, font=("Arial", 10), width=20)
    listCodigos.place(x=25, y=200)

    label8 = Label (ventanaConsultaPlan, text= "Vigencia del plan: ")
    label8.place(x=10, y=400)
    label8.config(font=("Arial", 12, BOLD))

    label9 = Label (ventanaConsultaPlan, text= "Correo: ")
    label9.place(x=10, y=450)
    label9.config(font=("Arial", 12, BOLD))

    correo = ttk.Entry (ventanaConsultaPlan, textvariable="correo", font=("Arial", 12), width=20)
    correo.place(x=75, y=450)

    seleccion3 = Button (ventanaConsultaPlan, text = "Generar PDF y enviar correo",  font=("Arial", 10))
    seleccion3.place(x=275, y=445 )

    label1 = Label (ventanaConsultaPlan, text= "Nombre del curso:")
    label1.place(x=175, y=175)
    label1.config(font=("Arial", 10, BOLD))
    listNombreCurso = Listbox(ventanaConsultaPlan, font=("Arial", 10), width=20)
    listNombreCurso.place(x=175, y=200)

    label2 = Label (ventanaConsultaPlan, text= "Bloque:")
    label2.place(x=325, y=175)
    label2.config(font=("Arial", 10, BOLD))
    listBloque = Listbox(ventanaConsultaPlan, font=("Arial", 10), width=20)
    listBloque.place(x=325, y=200)

    label3 = Label (ventanaConsultaPlan, text= "Horas lectivas:")
    label3.place(x=475, y=175)
    label3.config(font=("Arial", 10, BOLD))
    listhoras = Listbox(ventanaConsultaPlan, font=("Arial", 10), width=20)
    listhoras.place(x=475, y=200)

    label4 = Label (ventanaConsultaPlan, text= "Creditos:")
    label4.place(x=625, y=175)
    label4.config(font=("Arial", 10, BOLD))
    listCreditos = Listbox(ventanaConsultaPlan, font=("Arial", 10), width=20)
    listCreditos.place(x=625, y=200)
    listCreditos.insert(1, *lista)





    def enviarcorreo():
        # import necessary packages
 

        
        # create message object instance
        msg = MIMEMultipart()
        
        
        message =""
        
        # setup the parameters of the message
        password = "mxpxgvtpprburcmb"
        msg['From'] = "gestorplanesdeestudio2022@gmail.com"
        msg['To'] = ""
        msg['Subject'] = "Plan de estudios Consultado"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        #create server
        server = smtplib.SMTP('smtp.gmail.com: 587')
        
        server.starttls()
        
        # Login Credentials for sending the mail
        server.login(msg['From'], password)
        
        
        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        
        server.quit()
        
        print ("successfully sent email to %s:" % (msg['To']))

    registrarButton = Button(ventanaConsultaPlan, text = "Volver",  font=("Arial", 12), width=15, command=volverMenu)
    registrarButton.place(x=350,y=550)


    ventanaConsultaPlan.mainloop()
ventanaConsultaPlan()

          