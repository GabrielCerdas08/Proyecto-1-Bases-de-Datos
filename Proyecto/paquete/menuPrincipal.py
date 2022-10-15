
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD



def ventanaMenu():
     ventanaMenu= tk.Tk()
     ventanaMenu.title ("Menú principal")
     ventanaMenu.config (width=800, height=540)
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
          
          
          
     planButton = Button(ventanaMenu, text = "Crear Plan de Estudios", command=irRegistrarPlan, font=("Arial", 12, BOLD), width=20 )
     planButton.place(x=200,y=200)

     cursoButton = Button(ventanaMenu, text = "Registro de Cursos", command=irRegistrarCurso, font=("Arial", 12, BOLD), width=20 )
     cursoButton.place(x=200,y=300)

     escuelaButton = Button(ventanaMenu, text = "Registro de Escuela o Área Académica", command=irRegistrarEscuela, font=("Arial", 12, BOLD), width=20 )
     escuelaButton.place(x=200,y=400)

     asignarButton = Button(ventanaMenu, text = "Asignar requistos y correquistos a un curso", command=irAsignarRequisitos, font=("Arial", 12, BOLD), width=20 )
     asignarButton.place(x=200,y=500)

     ventanaMenu.mainloop()

ventanaMenu()