
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD



def ventanaMenu():
     ventanaMenu= tk.Tk()
     ventanaMenu.title ("Menú principal")
     ventanaMenu.config (width=400, height=250)
     ventanaMenu.resizable(False, False)

     def irRegistrarPlan():
          import registrarPlan
          registrarPlan.ventanaPlan()

     def irRegistrarCurso():

          import registrarCurso
          
          registrarCurso.ventanaCurso()

     def irRegistrarEscuela():

          import registrarEscuela
          registrarEscuela.ventanaEscuela()

     def irAsignarRequisitos():

          import asignarRequisitos
          asignarRequisitos.ventanaRequisitos()

     def irConsulta():

          import consultarPlanes
          consultarPlanes.ventanaConsultaPlan()

     def irConsultaAdicional():

          import consultasAdicionales
          consultasAdicionales.ventanaConsultaAdicional()

     def irEliminarCurso():

          import eliminarCurso
          eliminarCurso.ventanaEliminarCurso()

     def irElCursoPLan():

          import eliminarPlan
          eliminarPlan.ventanaEliminarCursoPlan()

     def irElCursoRe():

          import eliminarRequisito
          eliminarRequisito.ventanaEliminarCursoReque()
          
     def volver():
          ventanaMenu.withdraw()
          import inicio
          inicio.ventanaInicio()

     volverAButton = Button(ventanaMenu, text = "Volver", command=volver, font=("Arial", 8, BOLD), width=40 )
     volverAButton.place(x=50,y=220)
          
     planButton = Button(ventanaMenu, text = "Crear Plan de Estudios", command=irRegistrarPlan, font=("Arial", 8, BOLD), width=40)
     planButton.place(x=50,y=10)

     cursoButton = Button(ventanaMenu, text = "Registro de Cursos", command=irRegistrarCurso, font=("Arial", 8, BOLD), width=40 )
     cursoButton.place(x=50,y=40)

     escuelaButton = Button(ventanaMenu, text = "Registro de Escuela o Área Académica", command=irRegistrarEscuela, font=("Arial", 8, BOLD), width=40)
     escuelaButton.place(x=50,y=70)

     asignarButton = Button(ventanaMenu, text = "Asignar requistos y correquistos a un curso", command=irAsignarRequisitos, font=("Arial", 8, BOLD), width=40 )
     asignarButton.place(x=50,y=100)


     eliminarCursoButton = Button(ventanaMenu, text = "Eliminar curso", command=irEliminarCurso, font=("Arial", 8, BOLD), width=40 )
     eliminarCursoButton.place(x=50,y=130)

     eliminarCursoPlanButton = Button(ventanaMenu, text = "Eliminar relacion de curso con plan de estudios", command=irElCursoPLan, font=("Arial", 8, BOLD), width=40 )
     eliminarCursoPlanButton.place(x=50,y=160)

     eliminarCursoRequeButton = Button(ventanaMenu, text = "Eliminar relacion de curso con requesitos", command=irElCursoRe, font=("Arial", 8, BOLD), width=40 )
     eliminarCursoRequeButton.place(x=50,y=190)

     ventanaMenu.mainloop()

ventanaMenu()