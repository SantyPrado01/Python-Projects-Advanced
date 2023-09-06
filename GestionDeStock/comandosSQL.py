import sqlite3

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

from funcion_agregar import * 
from funcion_buscar import *
from funcion_editar import *

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





