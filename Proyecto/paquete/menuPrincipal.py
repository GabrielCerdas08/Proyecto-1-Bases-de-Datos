
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD



def ventanaMenu():
     ventanaMenu= tk.Tk()
     ventanaMenu.title ("Menú principal")
     ventanaMenu.config (width=400, height=300)
     ventanaMenu.resizable(False, False)

    
     def irConsulta():
          ventanaMenu.destroy()
          import consultarPlanes
          consultarPlanes.ventanaConsultaPlan()

     def irConsultaAdicional():
          ventanaMenu.destroy()
          import consultasAdicionales
          consultasAdicionales.ventanaConsultaAdicional()


          
 
     def volver():
          ventanaMenu.withdraw()
          import inicio
          inicio.ventanaInicio()

     consultarButton = Button(ventanaMenu, text = "Consultar plan de estudios", command=irConsulta, font=("Arial", 8, BOLD), width=40 )
     consultarButton.place(x=50,y=130)

     consultarAButton = Button(ventanaMenu, text = "Consultas adicionales", command=irConsultaAdicional, font=("Arial", 8, BOLD), width=40 )
     consultarAButton.place(x=50,y=160)

     volverAButton = Button(ventanaMenu, text = "Volver", command=volver, font=("Arial", 8, BOLD), width=40 )
     volverAButton.place(x=50,y=190)



     ventanaMenu.mainloop()

ventanaMenu()