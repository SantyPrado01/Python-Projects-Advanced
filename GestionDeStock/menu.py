from tkinter import *
from funciones import *

ventana = Tk()

ventana.title('Almacen')

tiutlo = Label(ventana, text='Gestion de Stock', font=32)
tiutlo.grid(row=0, columnspan=3)

boton_agregar = Button(ventana, text='Agregar Productos', command=lambda:agregar_producto(ventana))
boton_agregar.grid(row=1, column=0)

boton_buscar = Button(ventana, text='Buscar Producto', command=lambda:buscar_producto(ventana))
boton_buscar.grid(row=1, column=1)

boton_eliminar = Button(ventana, text='Eliminar Producto', command=lambda:eliminar_producto(ventana))
boton_eliminar.grid(row=1, column=2)


ventana.mainloop()