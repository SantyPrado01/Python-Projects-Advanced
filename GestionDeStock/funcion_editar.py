import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

from comandosSQL import *
from funcion_agregar import * 
from funcion_buscar import *
from funcion_editar import *


def eliminar_productos(tree):

    item_seleccionado = tree.selection()

    if item_seleccionado:
        
        fila_seleccionada = tree.item(item_seleccionado)
        datos = fila_seleccionada['values']

        base_datos =sqlite3.connect('almacen.bd')
        cursor = base_datos.cursor()

        cursor.execute("DELETE FROM producto WHERE producto_id=?", (datos[0],))

        base_datos.commit()

        base_datos.close()

        tree.delete(item_seleccionado)

        messagebox.showinfo('Completado','El producto ha sido eliminado con éxito.')


def mostrar_formulario_edicion(tree):

    ventana_emergente = Toplevel()

    ventana_emergente.resizable(width=False, height=False)

    ventana_emergente.title('Editar Producto')

    item_seleccionado = tree.selection()

    if item_seleccionado:

        fila_seleccionada = tree.item(item_seleccionado)
        datos = fila_seleccionada['values']

        titulo = Label(ventana_emergente, text='Editar Producto', font=65)
        titulo.grid(row=0, columnspan=2, padx=10, pady=10)

        titulo_producto = Label(ventana_emergente, text='Nombre Producto', font=45)
        titulo_producto.grid(row=1, column=0, padx=5, pady=5)

        nombre_producto = Entry(ventana_emergente, font=45)
        nombre_producto.grid(row=1, column=1)
        nombre_producto.insert(0, datos[1])  

        titulo_precio = Label(ventana_emergente, text='Precio', font=45)
        titulo_precio.grid(row=2, column=0, padx=5, pady=5)

        precio_producto = Entry(ventana_emergente, font=45)
        precio_producto.grid(row=2, column=1)
        precio_producto.insert(0, datos[2]) 

        titulo_stock = Label(ventana_emergente, text='Stock', font=45)
        titulo_stock.grid(row=3, column=0, padx=5, pady=5)

        stock_producto = Entry(ventana_emergente, font=45)
        stock_producto.grid(row=3, column=1)
        stock_producto.insert(0, datos[3])  

        titulo_marca = Label(ventana_emergente, text='Marca', font=45)
        titulo_marca.grid(row=4, column=0)

        marcas_opciones = ['Seleccionar Marca', 'Arcor', 'Marolio', 'Serenisima', 'Knor', 'Natura']

        marca_seleccionada = StringVar()
        marca_seleccionada.set(datos[4])  

        marca_producto = OptionMenu(ventana_emergente, marca_seleccionada, *marcas_opciones)
        marca_producto.grid(row=4, column=1)

        titulo_categoria = Label(ventana_emergente, text='Categoria', font=45)
        titulo_categoria.grid(row=5, column=0)

        categorias_opciones = ['Seleccionar Categoria', 'Almacen', 'Bebidas', 'Lacteos', 'Golosinas', 'Aceites', 'Otros']

        categoria_seleccionada = StringVar()
        categoria_seleccionada.set(datos[5])  

        categoria_producto = OptionMenu(ventana_emergente, categoria_seleccionada, *categorias_opciones)
        categoria_producto.grid(row=5, column=1)

        def guardar_cambios():
            nombre = nombre_producto.get()
            precio = precio_producto.get()
            stock = stock_producto.get()

            marca = marca_seleccionada.get()
            categoria = categoria_seleccionada.get()

            base_datos = sqlite3.connect('almacen.bd')
            cursor = base_datos.cursor()
            # Obtiene los IDs de marca y categoría
            cursor.execute("SELECT marca_id FROM marca WHERE nombre = ?", (marca,))
            marca_id = cursor.fetchone()[0]

            cursor.execute("SELECT categoria_id FROM categoria WHERE nombre = ?", (categoria,))
            categoria_id = cursor.fetchone()[0]
            
            cursor.execute("UPDATE producto SET nombre=?, precio=?, stock=?, marca_id=?, categoria_id=? WHERE producto_id=?", (nombre, precio, stock, marca_id, categoria_id, datos[0]))
            base_datos.commit()

    boton_guardar = Button(ventana_emergente, text='Guardar Cambios', command=guardar_cambios, font=45)
    boton_guardar.grid(row=6, columnspan=2, padx=5, pady=5)