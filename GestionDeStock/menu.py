from tkinter import *
from funciones import *

ventana = Tk()
ventana.resizable(width=False, height=False)
ventana.title('Almacen')

tiutlo = Label(ventana, text='Gestion de Stock', font=60)
tiutlo.grid(row=0, columnspan=3, padx=10, pady=10)

boton_agregar = Button(ventana, text='Agregar Productos', command=lambda:agregar_producto(ventana), font=45)
boton_agregar.grid(row=1, column=0, padx=10, pady=10)

boton_mostrar_productos = Button(ventana, text='Mostrar Productos', command=lambda:producto_buscar)

boton_buscar = Button(ventana, text='Buscar Producto', command=lambda:buscar_producto(ventana), font=45)
boton_buscar.grid(row=1, column=1, padx=10, pady=10)

ventana.mainloop()