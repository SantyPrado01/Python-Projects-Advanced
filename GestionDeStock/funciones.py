import sqlite3

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

base_datos = sqlite3.connect('almacen.bd')
cursor = base_datos.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS categoria(
        categoria_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(255) NOT NULL          
    )   
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS marca(
        marca_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(255) NOT NULL          
    )   
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS marcaxproducto(
        producto_id INT,
        marca_id INT,
        PRIMARY KEY (producto_id, marca_id),
        FOREIGN KEY (producto_id) REFERENCES productos(producto_id),
        FOREIGN KEY (marca_id) REFERENCES marcas(marca_id)
    )   
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS categoriaxproducto(
        producto_id INT,
        categoria_id INT,
        PRIMARY KEY (producto_id, categoria_id),
        FOREIGN KEY (producto_id) REFERENCES productos(producto_id),
        FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
    )   
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS producto(
        producto_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(255) NOT NULL,
        precio VARCHAR(255) NOT NULL,
        stock VARCHAR(255) NOT NULL,
        marca_id INT,
        categoria_id INT,
        FOREIGN KEY (marca_id) REFERENCES marcas(marca_id),
        FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)  
                   
    )
''')

base_datos.commit()
base_datos.close()

def agregar_producto(ventana):
    ventana_emergente = Toplevel(ventana)
    ventana_emergente.resizable(width=False, height=False)

    ventana_emergente.title('Agregar Producto')

    titulo = Label(ventana_emergente, text='Agregar Producto', font=60)
    titulo.grid(row=0, columnspan=2, padx=10, pady=10)

    titulo_producto = Label(ventana_emergente, text='Nombre Producto', font=45)
    titulo_producto.grid(row=1, column=0, padx=5, pady=5)

    nombre_producto = Entry(ventana_emergente, font=45)
    nombre_producto.grid(row=1, column=1, padx=5, pady=5)

    titulo_precio = Label(ventana_emergente, text='Precio', font=45)
    titulo_precio.grid(row=2, column=0, padx=5, pady=5)

    precio_producto = Entry(ventana_emergente, font=45)
    precio_producto.grid(row=2, column=1, padx=5, pady=5)

    titulo_stock = Label(ventana_emergente, text='Stock', font=45)
    titulo_stock.grid(row=3, column=0, padx=5, pady=5)

    stock_producto = Entry(ventana_emergente, font=45)
    stock_producto.grid(row=3, column=1, padx=5, pady=5)

    titulo_marca = Label(ventana_emergente, text='Marca', font=45)
    titulo_marca.grid(row=4, column=0, padx=5, pady=5)

    marcas_opciones = ['Seleccionar Marca', 'Arcor', 'Marolio', 'Serenisima', 'Knor', 'Natura']

    marca_seleccionada = StringVar()
    marca_seleccionada.set(marcas_opciones[0])

    marca_producto = OptionMenu(ventana_emergente, marca_seleccionada, *marcas_opciones)
    marca_producto.grid(row=4, column=1, padx=5, pady=5)

    titulo_categoria = Label(ventana_emergente, text='Categoria', font=45)
    titulo_categoria.grid(row=5, column=0, padx=5, pady=5)

    categorias_opciones = ['Seleccionar Categoria', 'Almacen', 'Bebidas', 'Lacteos', 'Golosinas', 'Aceites', 'Otros']

    categoria_seleccionada = StringVar()
    categoria_seleccionada.set(categorias_opciones[0])

    categoria_producto = OptionMenu(ventana_emergente, categoria_seleccionada, *categorias_opciones)
    categoria_producto.grid(row=5, column=1, padx=5, pady=5)

    base_datos = sqlite3.connect('almacen.bd')
    cursor = base_datos.cursor()

    def insertar_marca(marca):
        
        cursor.execute("INSERT OR IGNORE INTO marca (nombre) VALUES (?)", (marca,))
        base_datos.commit()

    def insertar_categoria(categoria):
        
        cursor.execute("INSERT OR IGNORE INTO categoria (nombre) VALUES (?)", (categoria,))
        base_datos.commit()

    def insertar_producto():
        nombre = nombre_producto.get()
        precio = precio_producto.get()
        stock = stock_producto.get()
        marca = marca_seleccionada.get()
        categoria = categoria_seleccionada.get()
    
        
        insertar_marca(marca)
        insertar_categoria(categoria)

        # Obtiene los IDs de marca y categoría
        cursor.execute("SELECT marca_id FROM marca WHERE nombre = ?", (marca,))
        marca_id = cursor.fetchone()
        cursor.execute("SELECT categoria_id FROM categoria WHERE nombre = ?", (categoria,))
        categoria_id = cursor.fetchone()

       
        cursor.execute("INSERT INTO producto (nombre, precio, stock, marca_id, categoria_id) VALUES (?, ?, ?, ?, ?)",
                   (nombre, precio, stock, marca_id[0], categoria_id[0]))

        base_datos.commit()
        messagebox.showinfo('Completado','El producto ha sido guardado con éxito.')

    boton_guardar = Button(ventana_emergente, text='Guardar Producto', command=insertar_producto)
    boton_guardar.grid(row=6, columnspan=2, padx=5, pady=5)


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
            tree = ttk.Treeview(ventana_emergente_2, columns=('ID',"Nombre", "Precio", "Stock","Marca", "Categoria"))
            
            tree.heading("#1", text='Identificador',anchor=tk.CENTER) 
            tree.heading("#2", text="Nombre", anchor=tk.CENTER)  # Centrar el encabezado 'Nombre'
            tree.heading("#3", text="Precio", anchor=tk.CENTER)  # Centrar el encabezado 'Precio'
            tree.heading("#4", text="Stock", anchor=tk.CENTER)
            tree.heading("#5", text="Marca", anchor=tk.CENTER)   # Centrar el encabezado 'Marca'
            tree.heading("#6", text="Categoria", anchor=tk.CENTER)  # Centrar el encabezado 'Categoria'
             
            
            for resultado in productos:
                id, nombre, precio, stock, marca_id, categoria_id = resultado

                cursor.execute("SELECT nombre FROM marca WHERE marca_id=?", (marca_id,))
                marca_nombre = cursor.fetchone()[0]

                cursor.execute("SELECT nombre FROM categoria WHERE categoria_id=?", (categoria_id,))
                categoria_nombre = cursor.fetchone()[0]

                tree.insert('','end', values=[id, nombre, precio, stock,marca_nombre, categoria_nombre])
                
            tree.grid(row=0, column=0, padx=10, pady=10)

            boton_editar = Button(ventana_emergente_2, text='Editar Producto', command=lambda:mostrar_formulario_edicion(), font=45)
            boton_editar.grid(row=1, column=0, padx=5, pady=5)

            boton_eliminar = Button(ventana_emergente_2, text='Eliminar Producto', command=lambda:eliminar_productos(), font=45)
            boton_eliminar.grid(row=1, column=2, padx=5, pady=5)


        base_datos.close()

    boton_buscar = Button(ventana_emergente, text='Buscar Producto', command=producto_buscar, font=45)
    boton_buscar.grid(row=2, columnspan=2, padx=5, pady=5)




def eliminar_productos():

    item_seleccionado = tree.selection()

    if item_seleccionado:
        fila_seleccionada = tree.item(item_seleccionado)
        datos = fila_seleccionada['values']

        base_datos =sqlite3.connect('almacen.bd')
        cursor = base_datos.cursor()

        cursor.execute("DELETE FROM producto WHERE producto_id=?", (datos[0],))

        base_datos.commit()

        base_datos.close()

        messagebox.showinfo('Completado','El producto ha sido eliminado con éxito.')


def mostrar_formulario_edicion():

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

            # Actualiza los datos del producto en la base de datos
            
            cursor.execute("UPDATE producto SET nombre=?, precio=?, stock=?, marca_id=?, categoria_id=? WHERE producto_id=?", (nombre, precio, stock, marca_id, categoria_id, datos[0]))
            base_datos.commit()

    boton_guardar = Button(ventana_emergente, text='Guardar Cambios', command=guardar_cambios, font=45)
    boton_guardar.grid(row=6, columnspan=2, padx=5, pady=5)