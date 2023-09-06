import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

from comandosSQL import *
from funcion_agregar import * 
from funcion_buscar import *
from funcion_editar import *


def buscar_producto(ventana):

    ventana_emergente = Toplevel(ventana)
    ventana_emergente.resizable(width=False, height=False)
    ventana_emergente.title('Buscar Producto')
    
    titulo = Label(ventana_emergente, text='Buscar Producto', font=65)
    titulo.grid(row=0, columnspan=7, padx=10, pady=10)

    criterio_busqueda = StringVar()
    criterio_busqueda.set('Nombre')
    opciones_busqueda = ["Nombre", "Marca", "Categoría"]

    opcion_busqueda = OptionMenu(ventana_emergente, criterio_busqueda, *opciones_busqueda)
    opcion_busqueda.grid(row=1, column=0, padx=5, pady=5)

    busqueda_entry = Entry(ventana_emergente, font=45)
    busqueda_entry.grid(row=1, column=1, padx=5, pady=5)

    def producto_buscar():

    # Obtén el criterio de búsqueda y el valor de entrada de búsqueda
        criterio = criterio_busqueda.get()
        valor_busqueda = busqueda_entry.get()
        base_datos = sqlite3.connect('almacen.bd')
        cursor = base_datos.cursor()
    # Realiza la búsqueda según el criterio seleccionado
        
        if criterio == "Nombre":
            cursor.execute("SELECT * FROM producto WHERE nombre LIKE ?", ('%' + valor_busqueda + '%',))
        elif criterio == "Marca":
            cursor.execute("SELECT * FROM producto WHERE marca_id IN (SELECT marca_id FROM marca WHERE nombre LIKE ?)", ('%' + valor_busqueda + '%',))
        elif criterio == "Categoría":
            cursor.execute("SELECT * FROM producto WHERE categoria_id IN (SELECT categoria_id FROM categoria WHERE nombre LIKE ?)", ('%' + valor_busqueda + '%',))
        
        productos = cursor.fetchall()
        
        if not productos:

            messagebox.showerror('Error', f'{productos} No Encontrado' )

        else:
            # Muestra los resultados 
            global tree
            ventana_emergente_2 = Toplevel()
            ventana_emergente_2.resizable(height=False, width=False)

            tree = ttk.Treeview(ventana_emergente_2, columns=('ID',"Nombre", "Precio", "Stock","Marca", "Categoria"))
            
            tree.column("#0", width=0, stretch=tk.NO)
            tree.heading("#1", text='Identificador',anchor=tk.CENTER) 
            tree.heading("#2", text="Nombre", anchor=tk.CENTER)  # Centrar el encabezado 'Nombre'
            tree.heading("#3", text="Precio", anchor=tk.CENTER)  
            tree.heading("#4", text="Stock", anchor=tk.CENTER)
            tree.heading("#5", text="Marca", anchor=tk.CENTER)   
            tree.heading("#6", text="Categoria", anchor=tk.CENTER)  
             
            for i in range(1, 7):  
                tree.column(f"#{i}", anchor=tk.CENTER)

            for resultado in productos:
                id, nombre, precio, stock, marca_id, categoria_id = resultado

                cursor.execute("SELECT nombre FROM marca WHERE marca_id=?", (marca_id,))
                marca_nombre = cursor.fetchone()[0]

                cursor.execute("SELECT nombre FROM categoria WHERE categoria_id=?", (categoria_id,))
                categoria_nombre = cursor.fetchone()[0]

                tree.insert('','end', values=[id, nombre, precio, stock,marca_nombre, categoria_nombre])
                
            tree.grid(row=0, column=0, padx=10, pady=10)

            boton_editar = Button(ventana_emergente_2, text='Editar Producto', command=lambda:mostrar_formulario_edicion(tree), font=45)
            boton_editar.grid(row=1, column=0, padx=5, pady=5)

            boton_eliminar = Button(ventana_emergente_2, text='Eliminar Producto', command=lambda:eliminar_productos(tree), font=45)
            boton_eliminar.grid(row=2, column=0, padx=5, pady=5)

        base_datos.close()

    boton_buscar = Button(ventana_emergente, text='Buscar Producto', command=producto_buscar, font=45)
    boton_buscar.grid(row=2, columnspan=2, padx=5, pady=5)


def buscar_todos():

    base_datos = sqlite3.connect('almacen.bd')
    cursor = base_datos.cursor()

    cursor.execute('SELECT * FROM producto')
    productos = cursor.fetchall()
        
    if not productos:
        messagebox.showerror('Error', f'{productos} No Encontrado' )
    else:
        ventana_emergente_2 = Toplevel()
        tree = ttk.Treeview(ventana_emergente_2, columns=('ID',"Nombre", "Precio", "Stock","Marca", "Categoria"))
        
        tree.column("#0", width=0, stretch=tk.NO)
        tree.heading("#1", text='Identificador',anchor=tk.CENTER) # Centrar el encabezado 'Nombre'
        tree.heading("#2", text="Nombre", anchor=tk.CENTER)  
        tree.heading("#3", text="Precio", anchor=tk.CENTER)  
        tree.heading("#4", text="Stock", anchor=tk.CENTER)
        tree.heading("#5", text="Marca", anchor=tk.CENTER)   
        tree.heading("#6", text="Categoria", anchor=tk.CENTER)  

        for i in range(1, 7):  
                tree.column(f"#{i}", anchor=tk.CENTER)

        for resultado in productos:

            id, nombre, precio, stock, marca_id, categoria_id = resultado

            cursor.execute("SELECT nombre FROM marca WHERE marca_id=?", (marca_id,))
            marca_nombre = cursor.fetchone()[0]

            cursor.execute("SELECT nombre FROM categoria WHERE categoria_id=?", (categoria_id,))
            categoria_nombre = cursor.fetchone()[0]

            tree.insert('','end', values=[id, nombre, precio, stock,marca_nombre, categoria_nombre])
                
        tree.grid(row=0, column=0, padx=10, pady=10)

        boton_editar = Button(ventana_emergente_2, text='Editar Producto', command=lambda:mostrar_formulario_edicion(tree), font=45)
        boton_editar.grid(row=1, column=0, padx=5, pady=5)

        boton_eliminar = Button(ventana_emergente_2, text='Eliminar Producto', command=lambda:eliminar_productos(tree), font=45)
        boton_eliminar.grid(row=2, column=0, padx=5, pady=5)

    base_datos.close()

