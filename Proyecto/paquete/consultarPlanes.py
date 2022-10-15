
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox, ttk
from unittest import result
import mysql.connector
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def ventanaPlan():
    ventanaPlan= tk.Toplevel()
    ventanaPlan.title ("Crear Plan de Estudios")
    ventanaPlan.config (width=800, height=650)
    ventanaPlan.resizable(False, False)


    entry4 = ttk.Entry (ventanaPlan, textvariable="codigoCursoPlan", font=("Arial", 12), width=20)
    entry4.place(x=150, y=500)

    entry5 = ttk.Entry (ventanaPlan, textvariable="codigoCursoPla", font=("Arial", 12), width=20)
    entry5.place(x=150, y=400)

    entry6 = ttk.Entry (ventanaPlan, textvariable="codigoCursoPl", font=("Arial", 12), width=20)
    entry6.place(x=150, y=300)

    def enviarcorreo():
        # import necessary packages
 

        
        # create message object instance
        msg = MIMEMultipart()
        
        
        message =entry6.get()
        
        # setup the parameters of the message
        password = "mxpxgvtpprburcmb"
        msg['From'] = "gestorplanesdeestudio2022@gmail.com"
        msg['To'] = entry4.get()
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

    registrarButton = Button(ventanaPlan, text = "Registrar",  font=("Arial", 12), width=15, command=enviarcorreo)
    registrarButton.place(x=350,y=550)


    ventanaPlan.mainloop()
ventanaPlan()

          