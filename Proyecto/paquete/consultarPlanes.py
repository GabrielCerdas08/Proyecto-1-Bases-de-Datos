
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox, ttk
from unittest import result
import mysql.connector
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

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
        body = '''Hello,
        This is the body of the email
        sicerely yours
        G.G.
        '''
        # put your email here
        sender = 'gestorplanesdeestudio2022@gmail.com'
        # get the password in the gmail (manage your google account, click on the avatar on the right)
        # then go to security (right) and app password (center)
        # insert the password and then choose mail and this computer and then generate
        # copy the password generated here
        password = 'mxpxgvtpprburcmb'
        # put the email of the receiver here
        receiver = correo.get()

        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = 'This email has an attacment, a pdf file'

        message.attach(MIMEText(body, 'plain'))

        pdfname = "Users\gaboc\OneDrive - Estudiantes ITCR\Documentos\GitHub\Proyecto-1-Bases-de-Datos\hoja.pdf"

        # open the file in bynary
        binary_pdf = open(pdfname, 'rb')

        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        # payload = MIMEBase('application', 'pdf', Name=pdfname)
        payload.set_payload((binary_pdf).read())

        # enconding the binary into base64
        encoders.encode_base64(payload)

        # add header with pdf name
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        message.attach(payload)

        #use gmail with port
        session = smtplib.SMTP('smtp.gmail.com', 587)

        #enable security
        session.starttls()

        #login with mail_id and password
        session.login(sender, password)

        text = message.as_string()
        session.sendmail(sender, receiver, text)
        session.quit()
        print('Mail Sent')

    seleccion3 = Button (ventanaConsultaPlan, text = "Generar PDF y enviar correo",command=enviarcorreo,  font=("Arial", 10))
    seleccion3.place(x=275, y=445 )

    registrarButton = Button(ventanaConsultaPlan, text = "Volver",  font=("Arial", 12), width=15, command=volverMenu)
    registrarButton.place(x=350,y=550)


    ventanaConsultaPlan.mainloop()
ventanaConsultaPlan()

          