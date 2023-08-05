import sqlite3
from tkinter import *
# Conexión a la base de datos (creará un archivo si no existe)
base_datos = sqlite3.connect('tareas.db')

# Crear tabla de tareas si no existe
base_datos.execute('''
    CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tarea TEXT NOT NULL,
        completed INTEGER NOT NULL DEFAULT 0
    )
''')

base_datos.commit()
base_datos.close()

# Función para mostrar todas las tareas en la base de datos
def mostrar_tareas(root):
    conn = sqlite3.connect('tareas.db')
    cursor = conn.execute('SELECT * FROM tareas')
    tareas = cursor.fetchall()
    conn.close()
    texto_mostrar = Label(root, text='Tareas:')
    texto_mostrar.grid(row=0, column=2)
    for tarea in tareas:
        tarea_id, tarea_desc, completed = tarea
        status = "Completada" if completed else "Pendiente"
        tareas = Label(root, text=f'{tarea_id}. [{status}] {tarea_desc}')
        tareas.grid(row=tarea_id, column=2)

# Función para agregar una nueva tarea
def agregar_tares(root, tarea_desc):
    conn = sqlite3.connect('tareas.db')
    conn.execute('INSERT INTO tareas (tarea) VALUES (?)', (tarea_desc,))
    conn.commit()
    conn.close()
    completado = Label(root, text='Tarea agregada con éxito.')
    completado.grid(row=10)
    mostrar_tareas(root)

# Función para eliminar una tarea
def elimanar_tareas(root, tarea_id):
    conn = sqlite3.connect('tareas.db')
    conn.execute('DELETE FROM tareas WHERE id = ?', (tarea_id,))
    conn.commit()
    conn.close()
    completado = Label(root,text="Tarea eliminada con éxito.")
    completado.grid(row=10)
    mostrar_tareas(root)

# Función para marcar una tarea como completada
def modificar_tareas(root, tarea_id):
    conn = sqlite3.connect('tareas.db')
    conn.execute('UPDATE tareas SET completed = 1 WHERE id = ?', (tarea_id,))
    conn.commit()
    conn.close()
    completado = Label(root,text="Tarea completada con éxito.")
    completado.grid(row=10)
    mostrar_tareas(root)