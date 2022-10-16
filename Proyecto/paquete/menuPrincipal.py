
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD



def ventanaMenu():
     ventanaMenu= tk.Tk()
     ventanaMenu.title ("Menú principal")
     ventanaMenu.config (width=400, height=300)
     ventanaMenu.resizable(False, False)

     def irRegistrarPlan():
          ventanaMenu.destroy()
          import registrarPlan
          registrarPlan.ventanaPlan()

     def irRegistrarCurso():
          ventanaMenu.destroy()
          import registrarCurso
          
          registrarCurso.ventanaCurso()

     def irRegistrarEscuela():
          ventanaMenu.destroy()
          import registrarEscuela
          registrarEscuela.ventanaEscuela()

     def irAsignarRequisitos():
          ventanaMenu.destroy()
          import asignarRequisitos
          asignarRequisitos.ventanaRequisitos()

     def irConsulta():
          ventanaMenu.destroy()
          import consultarPlanes
          consultarPlanes.ventanaConsultaPlan()

     def irConsultaAdicional():
          ventanaMenu.destroy()
          import consultasAdicionales
          consultasAdicionales.ventanaConsultaAdicional()

     def irEliminarCurso():
          ventanaMenu.destroy()
          import eliminarCurso
          eliminarCurso.ventanaEliminarCurso()

     def irElCursoPLan():
          ventanaMenu.destroy()
          import eliminarPlan
          eliminarPlan.ventanaEliminarCursoPlan()

     def irElCursoRe():
          ventanaMenu.destroy()
          import eliminarRequisito
          eliminarRequisito.ventanaEliminarCursoReque()
          
          
          
     planButton = Button(ventanaMenu, text = "Crear Plan de Estudios", command=irRegistrarPlan, font=("Arial", 8, BOLD), width=40)
     planButton.place(x=50,y=10)

     cursoButton = Button(ventanaMenu, text = "Registro de Cursos", command=irRegistrarCurso, font=("Arial", 8, BOLD), width=40 )
     cursoButton.place(x=50,y=40)

     escuelaButton = Button(ventanaMenu, text = "Registro de Escuela o Área Académica", command=irRegistrarEscuela, font=("Arial", 8, BOLD), width=40)
     escuelaButton.place(x=50,y=70)

     asignarButton = Button(ventanaMenu, text = "Asignar requistos y correquistos a un curso", command=irAsignarRequisitos, font=("Arial", 8, BOLD), width=40 )
     asignarButton.place(x=50,y=100)

     consultarButton = Button(ventanaMenu, text = "Consultar plan de estudios", command=irConsulta, font=("Arial", 8, BOLD), width=40 )
     consultarButton.place(x=50,y=130)

     consultarAButton = Button(ventanaMenu, text = "Consultas adicionales", command=irConsultaAdicional, font=("Arial", 8, BOLD), width=40 )
     consultarAButton.place(x=50,y=160)

     eliminarCursoButton = Button(ventanaMenu, text = "Eliminar curso", command=irEliminarCurso, font=("Arial", 8, BOLD), width=40 )
     eliminarCursoButton.place(x=50,y=190)

     eliminarCursoPlanButton = Button(ventanaMenu, text = "Eliminar relacion de curso con plan de estudios", command=irElCursoPLan, font=("Arial", 8, BOLD), width=40 )
     eliminarCursoPlanButton.place(x=50,y=220)

     eliminarCursoRequeButton = Button(ventanaMenu, text = "Eliminar relacion de curso con requesitos", command=irElCursoRe, font=("Arial", 8, BOLD), width=40 )
     eliminarCursoRequeButton.place(x=50,y=250)

     ventanaMenu.mainloop()

ventanaMenu()