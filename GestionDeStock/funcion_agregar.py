from tkinter import *
from tkinter import messagebox
from comandosSQL import *
from funcion_agregar import * 
from funcion_buscar import *
from funcion_editar import *

base_datos = sqlite3.connect('almacen.bd')

cursor = base_datos.cursor()

def agregar_producto(ventana):
    global ventana_emergente, marcas_opciones

    ventana_emergente= Toplevel(ventana)
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

    marcas_opciones = obtener_marcas_existentes()
  
    marca_seleccionada = StringVar()
    marca_seleccionada.set(marcas_opciones[0])

    marca_producto = OptionMenu(ventana_emergente, marca_seleccionada, *marcas_opciones)
    marca_producto.grid(row=4, column=1, padx=5, pady=5)

    agregar_marca = Button(ventana_emergente, text='+', font=45, command=lambda:crear_marca(ventana_emergente))
    agregar_marca.grid(row=4, column=3, padx=5, pady=5)

    titulo_categoria = Label(ventana_emergente, text='Categoria', font=45)
    titulo_categoria.grid(row=5, column=0, padx=5, pady=5)

    categorias_opciones = ['Seleccionar Categoria', 'Almacen', 'Bebidas', 'Lacteos', 'Golosinas', 'Aceites', 'Otros']

    categoria_seleccionada = StringVar()
    categoria_seleccionada.set(categorias_opciones[0])

    categoria_producto = OptionMenu(ventana_emergente, categoria_seleccionada, *categorias_opciones)
    categoria_producto.grid(row=5, column=1, padx=5, pady=5) 

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

        nombre_producto.delete(0, 'end')
        precio_producto.delete(0, 'end')
        stock_producto.delete(0, 'end')
        marca_seleccionada.set('Seleccionar Marca')
        categoria_seleccionada.set('Seleccionar Categoria')

    boton_guardar = Button(ventana_emergente, text='Guardar Producto', command=insertar_producto)
    boton_guardar.grid(row=6, columnspan=2, padx=5, pady=5)
    

def crear_marca(ventana_emergente):
   
    ventana_emergente_2 = Toplevel(ventana_emergente)
    ventana_emergente_2.title('Agregar Marca')
    ventana_emergente_2.resizable(height=False, width=False)

    titulo_agregar_marca = Label(ventana_emergente_2, text='Agregar Marca', font=45)
    titulo_agregar_marca.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

    marca_agregar_txt = Label(ventana_emergente_2, text='Marca', font=45)
    marca_agregar_txt.grid(row=1, column=0)

    marca_agregar = Entry(ventana_emergente_2, font=45)
    marca_agregar.grid(row=1, column=1, padx=5, pady=5)

    boton_agregar = Button(ventana_emergente_2, text='Agregar Marca', command=lambda:insertar_marca(marca_agregar.get()))
    boton_agregar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    marca = marca_agregar.get()
    if marca not in marcas_opciones:
        cursor.execute("INSERT OR IGNORE INTO marca (nombre) VALUES (?)", (marca,))
        base_datos.commit()
        messagebox.showinfo('Completado', 'La marca ha sido guardada con éxito.')

    ventana_emergente_2.destroy()

def obtener_marcas_existentes():
    cursor.execute("SELECT nombre FROM marca")
    marcas = cursor.fetchall()
    return ['Seleccionar Marca'] + [nombre[0] for nombre in marcas]

