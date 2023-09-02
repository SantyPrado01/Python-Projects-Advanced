import sqlite3
from tkinter import *

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
    ventana_emergente.title('Agregar Producto')

    titulo = Label(ventana_emergente, text='Agregar Producto')
    titulo.grid(row=0, column=0)

    titulo_producto = Label(ventana_emergente, text='Nombre Producto')
    titulo_producto.grid(row=1, column=0)

    nombre_producto = Entry(ventana_emergente)
    nombre_producto.grid(row=1, column=1)

    titulo_precio = Label(ventana_emergente, text='Precio')
    titulo_precio.grid(row=2, column=0)

    precio_producto = Entry(ventana_emergente)
    precio_producto.grid(row=2, column=1)

    titulo_stock = Label(ventana_emergente, text='Stock')
    titulo_stock.grid(row=3, column=0)

    stock_producto = Entry(ventana_emergente)
    stock_producto.grid(row=3, column=1)

    titulo_marca = Label(ventana_emergente, text='Marca')
    titulo_marca.grid(row=4, column=0)

    marcas_opciones = ['Seleccionar Marca', 'Arcor', 'Marolio', 'Serenisima', 'Knor', 'Natura']

    marca_seleccionada = StringVar()
    marca_seleccionada.set(marcas_opciones[0])

    marca_producto = OptionMenu(ventana_emergente, marca_seleccionada, *marcas_opciones)
    marca_producto.grid(row=4, column=1)

    titulo_categoria = Label(ventana_emergente, text='Categoria')
    titulo_categoria.grid(row=5, column=0)

    categorias_opciones = ['Seleccionar Categoria', 'Almacen', 'Bebidas', 'Lacteos', 'Golosinas', 'Aceites', 'Otros']

    categoria_seleccionada = StringVar()
    categoria_seleccionada.set(categorias_opciones[0])

    categoria_producto = OptionMenu(ventana_emergente, categoria_seleccionada, *categorias_opciones)
    categoria_producto.grid(row=5, column=1)

    base_datos = sqlite3.connect('almacen.bd')
    cursor = base_datos.cursor()

    def insertar_marca(marca):
        # Inserta la marca en la tabla 'marca' si no existe
        cursor.execute("INSERT OR IGNORE INTO marca (nombre) VALUES (?)", (marca,))
        base_datos.commit()

    def insertar_categoria(categoria):
        # Inserta la categoría en la tabla 'categoria' si no existe
        cursor.execute("INSERT OR IGNORE INTO categoria (nombre) VALUES (?)", (categoria,))
        base_datos.commit()

    def insertar_producto():
        nombre = nombre_producto.get()
        precio = precio_producto.get()
        stock = stock_producto.get()
        marca = marca_seleccionada.get()
        categoria = categoria_seleccionada.get()
    
        # Inserta la marca y la categoría si no existen
        insertar_marca(marca)
        insertar_categoria(categoria)

        # Obtiene los IDs de marca y categoría
        cursor.execute("SELECT marca_id FROM marca WHERE nombre = ?", (marca,))
        marca_id = cursor.fetchone()
        cursor.execute("SELECT categoria_id FROM categoria WHERE nombre = ?", (categoria,))
        categoria_id = cursor.fetchone()

        # Inserta el producto en la tabla 'producto'
        cursor.execute("INSERT INTO producto (nombre, precio, stock, marca_id, categoria_id) VALUES (?, ?, ?, ?, ?)",
                   (nombre, precio, stock, marca_id[0], categoria_id[0]))

        # Guarda los cambios en la base de datos
        base_datos.commit()
    boton_guardar = Button(ventana_emergente, text='Guardar Producto', command=insertar_producto)
    boton_guardar.grid(row=6, columnspan=2)


def buscar_producto(ventana):
    ventana_emergente = Toplevel(ventana)
    ventana_emergente.title('Buscar Producto')
    
    titulo = Label(ventana_emergente, text='Buscar Producto')
    titulo.grid(row=0, column=0)

    criterio_busqueda = StringVar()
    criterio_busqueda.set('Nombre')
    opciones_busqueda = ["Nombre", "Marca", "Categoría"]

    opcion_busqueda = OptionMenu(ventana_emergente, criterio_busqueda, *opciones_busqueda)
    opcion_busqueda.grid(row=1, column=0)

    busqueda_entry = Entry(ventana_emergente)
    busqueda_entry.grid(row=1, column=1)

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

        resultados = cursor.fetchall()

        # Muestra los resultados (esto depende de cómo quieras mostrarlos en tu interfaz)
        for resultado in resultados:
            print(resultado)

    # Cierra la conexión a la base de datos cuando hayas terminado
        base_datos.close()

    boton_buscar = Button(ventana_emergente, text='Buscar Producto', command=producto_buscar)
    boton_buscar.grid(row=2, columnspan=2)



def eliminar_producto(ventana):
    ventana_emergente = Toplevel(ventana)
    ventana_emergente.title('Eliminar Producto')