from funciones import *
from tkinter import *

#-------------------------------------------- TKINTER -------------------------------------------------

root = Tk()

root.title('Control de Tareas')

icon_path = "img/logo.ico"  
root.iconbitmap(icon_path)

tareas_txt = Label(root, text='Esta aplicacion te permite llevar un control de tus tareas. Agregando, Eliminando y Completando tareas.').grid()

agregar_txt = Label(root, text='Que tarea deseas agregar?').grid(row=2)
agregar_entry = Entry(root)
agregar_entry.grid(row=3, column=0)

boton_tareas_agregar = Button(root, text='Agregar Tarea', command= lambda:agregar_tares(root, agregar_entry.get()))
boton_tareas_agregar.grid(row=3, column=1)

eliminar_txt = Label(root, text='Eliminar Tareas. Escriba el numero de la tarea a eliminar.').grid(row=5)
eliminar_entry = Entry(root)
eliminar_entry.grid(row=6)

boton_tareas_eliminar = Button(root, text='Eliminar Tarea', command= lambda:elimanar_tareas(root, eliminar_entry.get()))
boton_tareas_eliminar.grid(row=6, column=1)

completar_txt = Label(root, text='Completar Tareas. Escriba el numero de la tarea a eliminar.').grid(row=7)
completar_entry =Entry(root)
completar_entry.grid(row=8)
boton_tareas_completar = Button(root, text='Completar Tarea', command= lambda:modificar_tareas(root, completar_entry.get()))
boton_tareas_completar.grid(row=8, column=1)

boton_tareas_mostrar = Button(root, text='Mostrar Tareas', command= lambda:mostrar_tareas(root))
boton_tareas_mostrar.grid(row=9, column=0)

root=mainloop()


