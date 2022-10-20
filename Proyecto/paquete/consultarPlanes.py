
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


    
    def volverMenu():
        ventanaConsultaPlan.withdraw()

    def getCodigo():
        global codigo
        codigo = " "
        nombre = "'"+str(combo1.get())+"'"

        mycursorGetCodigo = conexion.cursor()
        mycursorGetCodigo.execute("SELECT codigo_area_academica FROM area_academica WHERE nombre="+ nombre)
        myresult = mycursorGetCodigo.fetchone()
        for x in myresult:
            codigo = x

        messagebox.showinfo(message="Se ha seleccionado la escuela", title= "¡Escuela selccionada!")

        if codigo == "":
            messagebox.showwarning(message="Debe de llenar todos los espacios", title="Datos incompletos")
        else:
            combo2.delete(0, END)
            mycursorBusqueda = conexion.cursor()
            mycursorBusqueda.execute ("SELECT numero_plan FROM plan_estudio WHERE codigo_area_academica ="+"'"+codigo+"'")
            listaplanes = [i[0]for i in mycursorBusqueda.fetchall()]
            combo2.configure(values=listaplanes)


    def getplan():
        global         codigocurso 

        codigocurso = " "
        fecha = ""
        nombre = "'"+str(combo2.get())+"'"

        mycursorGetCodigoplan = conexion.cursor()
        mycursorGetCodigoplan.execute("SELECT id_curso FROM intermedia_planestudio_curso WHERE numero_plan="+ nombre)
        myresult = mycursorGetCodigoplan.fetchone()
        for x in myresult:
            codigocurso = x

        mycursorGetCodigoplan2 = conexion.cursor()
        mycursorGetCodigoplan2.execute("SELECT fecha_entrada_vigencia FROM plan_estudio WHERE numero_plan="+ nombre)
        myresult2 = mycursorGetCodigoplan2.fetchone()
        for x in myresult2:
            fecha = x
            label8.configure(text="Vigencia del plan: "+ fecha )

        messagebox.showinfo(message="Se ha seleccionado el plan", title= "¡Plan selccionado!")



    label5 = Label (ventanaConsultaPlan, text= "Consultar Plan de estudios")
    label5.place(x=150, y=10)
    label5.config(font=("Verdana", 24, BOLD))

    label6 = Label (ventanaConsultaPlan, text= "Escuela del curso:")
    label6.place(x=10, y=70)
    label6.config(font=("Arial", 12, BOLD))

    
    combo1 = ttk.Combobox (ventanaConsultaPlan, state="readonly", width=25, values=lista)
    combo1.place(x=180, y=70)

    seleccion = Button (ventanaConsultaPlan, text = "Selecionar", command=getCodigo, font=("Arial", 10), width=10)
    seleccion.place(x=375, y=65 )

    label7 = Label (ventanaConsultaPlan, text= "Codigo del plan de estudios:")
    label7.place(x=10, y=115)
    label7.config(font=("Arial", 12, BOLD))

    combo2 = ttk.Combobox (ventanaConsultaPlan, state="readonly", width=25, values=lista)
    combo2.place(x=240, y=115)

    seleccion2 = Button (ventanaConsultaPlan, text = "Selecionar",command=getplan,  font=("Arial", 10), width=10)
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


    def generarpdf():


        from fpdf import FPDF

        # datos para usar
        lista_datos = [
            (1, 'Carlos', 'carlos@gmail.com', '2020-02-25'),
            (2, 'Jose', 'jose@gmail.com', '2019-03-12'),
            (3, 'Marcos', 'marcos@gmail.com', '2018-01-31'),
            (4, 'Luz', 'luz@gmail.com', '2017-02-15'),
            (5, 'Elmer', 'elmer@gmail.com', '2016-11-23'),
            ]

        pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
        pdf.add_page()

        # TEXTO
        pdf.set_font('Arial', '', 15)

        # titulo
        pdf.cell(w = 0, h = 15, txt = 'Reporte de plan de estudios', border = 1, ln=1,
                align = 'C', fill = 0)

        # encabezado
        pdf.cell(w = 20, h = 15, txt = 'Codigo', border = 1,
                align = 'C', fill = 0)

        pdf.cell(w = 40, h = 15, txt = 'Nombre', border = 1,
                align = 'C', fill = 0)

        pdf.cell(w = 70, h = 15, txt = 'Horas', border = 1,
                align = 'C', fill = 0)

        pdf.multi_cell(w = 0, h = 15, txt = 'Creditos', border = 1,
                align = 'C', fill = 0)


        # valores
        for valor in lista_datos:

            pdf.cell(w = 20, h = 9, txt = str(valor[0]), border = 1,
                    align = 'C', fill = 0)

            pdf.cell(w = 40, h = 9, txt = valor[1], border = 1,
                    align = 'C', fill = 0)

            pdf.cell(w = 70, h = 9, txt = valor[2], border = 1,
                    align = 'C', fill = 0)

            pdf.multi_cell(w = 0, h = 9, txt = valor[3], border = 1,
                    align = 'C', fill = 0)


        pdf.output('Proyecto\PDFS\ '+ combo2.get()+ ".pdf")


    def enviarcorreo():
        body = '''El siguiente correo se le envia para dar con el reporte del plan de estudios solicitado, se adjunta el respectivo archivo pdf
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
        message['Subject'] = 'Plan de estudios'

        message.attach(MIMEText(body, 'plain'))

        pdfname = 'Proyecto\PDFS\ '+ combo2.get()+ ".pdf"

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

        messagebox.showinfo(message="Correo enviado", title= "¡Se ha enviado!")
        

    def enviarYcrear():
        generarpdf()
        enviarcorreo()

    seleccion3 = Button (ventanaConsultaPlan, text = "Generar PDF y enviar correo",command=enviarYcrear,  font=("Arial", 10))
    seleccion3.place(x=275, y=445 )

    registrarButton = Button(ventanaConsultaPlan, text = "Volver",  font=("Arial", 12), width=15, command=volverMenu)
    registrarButton.place(x=350,y=550)


    ventanaConsultaPlan.mainloop()
ventanaConsultaPlan()

          