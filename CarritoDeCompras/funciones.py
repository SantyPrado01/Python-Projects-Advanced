from datetime import date
from datetime import datetime
#Creando Productos
class Producto(object):
    def __init__(self, nombre, marca, codigo, stock, precio, color, descripcion):
        self.nombre = nombre
        self.marca = marca
        self.codigo = codigo
        self.stock = stock
        self.precio = precio
        self.color = color
        self.descripcion = descripcion
        
    def informacion_detallada(self):
        return f'La informacion del producto es: \n Nombre: {self.nombre}\n Marca: {self.marca} \n Codigo: {self.codigo} \n Stock: {self.stock} \n Precio: {self.precio} \n Color: {self.color} \n Descripcion: {self.descripcion}'
    
    def informacion_sencilla(self):
        return f'La informacion breve del producto es: \n Nombre: {self.nombre} \n Precio: {self.precio} \n Codigo: {self.codigo} \n Stock: {self.stock}'
    
    def obtener_nombre(self):
        return self.nombre
    
    def __str__(self):
        return self.obtener_nombre()
    
    def modificar_stock(self, cantidad):
        self.stock -= cantidad   
    
    def verificar_stock(self, cantidad):
        if self.stock >= cantidad:
            return True
        else:
            return False
    
class CarritoCompras:
    def __init__(self):
        self.productos = []
        self.monto_total = 0
        
    def agregar_carrito(self,producto, cantidad):
        if producto.verificar_stock(cantidad):
            producto.modificar_stock(cantidad)
            precio_total = producto.precio*cantidad
            self.monto_total += precio_total
            self.productos.append((producto, cantidad))
            print('=='*45)
            print(f'{cantidad} unidad(es) de {producto.nombre} agregada(s) al carrito.')
            print('=='*45)
        else:
            print('=='*45)
            print(f'No hay suficiente stock de {producto.nombre}.')
            print('=='*45)

    def mostrar_carrito(self):
        
        if len(self.productos) == 0:
            print('No hay productos en el carrito.')
            print('=='*45)
            return(False)
        else:
            print('=='*45)
            nombre = input('A nombre de quien realizamos la factura?: ')
            
            print('Productos en el carrito:')
            
            for producto, cantidad in self.productos:

                print(f'{cantidad} unidad(es) de {producto.nombre}')
                
            print(f'El monto total a pagar es: ${self.monto_total}')
            print('=='*45)
            print(f'Factura B Cliente: {nombre} Fecha: {date.today()}') 
            return(True) 
        
    def mostrar_carrito_dos(self):
        
        print('=='*45)
            
        print('Productos en el carrito:')
            
        for producto, cantidad in self.productos:

            print(f'{cantidad} unidad(es) de {producto.nombre}')
                
        print(f'El monto total a pagar es: ${self.monto_total}')
        print('=='*45)
  
                
carrito = CarritoCompras()
     
productos = [
    Producto('MacBook', 'Apple', 1001, 10, 1000, 'Gris', 'Procesador M1, 8GB Ram, 256Gb SSD, Pantalla 13 Pulgadas'),
    Producto('iPad Air', 'Apple', 1002, 5, 900, 'Azul Marino', 'Procesador M1, 4Gb Ram, 256GB Almacenamiento, Pantalla 10,1 Pulgadas'),
    Producto('AirPods', 'Apple', 1003, 12, 100, 'Blacno', 'Bateria 10hs, Estuche de Carga, Cargador No Incluido'),
    Producto('Termo', 'Stanley', 1004, 8, 100, 'Negro', ''),
]


def opcion_uno():
    
    for Producto in productos:
        print('=='*45)
        print(Producto.informacion_detallada())
        print('=='*45)
    carrito_agregar()

def opcion_dos():
    
    for Producto in productos:
        print('=='*45)
        print(Producto.informacion_sencilla())
        print('=='*45)
    carrito_agregar()
        
def opcion_tres():
    while True:
        try:
            codigo = int(input('Ingresar código de producto a buscar: '))
            producto_encontrado = None

            for Producto in productos:
                if Producto.codigo == codigo:
                    producto_encontrado = Producto
                    break

            if producto_encontrado:
                print(producto_encontrado.informacion_detallada())
                carrito_agregar()
            else:
                print('Producto no encontrado')
                print('=='*45)
                
        except ValueError:
            print('No es código válido')
            print('=='*45)
        else:
            break
      
def opcion_cuatro():
    while True:
        try:
            codigo_producto = int(input('¿Qué producto desea agregar al carrito? (Ingrese el código del producto): '))
            producto = buscar_producto_dos(codigo_producto)

            if producto:
                unidades = int(input(f'¿Cuántas unidades de {producto.nombre} va a llevar?: '))
                carrito.agregar_carrito(producto, unidades)
            else:
                print('Producto no encontrado')
                print('=='*45)
                
        except ValueError:
            print('No es un código válido')
            print('=='*45)
            
        else:
            break
    
def opcion_cinco():
    
    if carrito.mostrar_carrito() == True:
        modificar_carrito()
            
 
def buscar_producto_dos(a):
    producto_encontrado = None
    for Producto in productos:
        if Producto.codigo == a:
            producto_encontrado = Producto
            break
    if producto_encontrado:
        return(producto_encontrado)
    else:
        print('Producto no encontrado')
        print('=='*45)
        return(False)
    
def carrito_agregar():
    while True:
        try:
            opcion = int(input('Desea agregar algun producto al carrito? (Si --> 1, No --> 2): '))
            if opcion == 1:
                opcion_cuatro()
            else:
                print('=='*45)
                print('Volviendo al menu')
                print('=='*45)
        except ValueError:
            print('No ingresaste una opcion valida, intenta nuevamente')
        else:
            break

def modificar_carrito():
    while True:
        try:
            modificar = int(input('Desea modificar el carrito? (Si --> 1, No --> 2): '))
            if modificar == 1:
                carrito.mostrar_carrito_dos()

                producto_modificar = int(input('Ingresa el código del producto a modificar: '))

                producto_encontrado = None
                index_producto = None
                for i, (producto, cantidad) in enumerate(carrito.productos):
                    if producto.codigo == producto_modificar:
                        producto_encontrado = producto
                        index_producto = i
                        break

                if producto_encontrado:
                    cantidad_nueva = int(input(f'Ingrese la nueva cantidad para el producto {producto_encontrado.nombre}: '))

                    if cantidad_nueva < cantidad:
                        cantidad_devolucion = cantidad - cantidad_nueva
                        producto_encontrado.modificar_stock(cantidad_devolucion)
                        carrito.productos[index_producto] = (producto_encontrado, cantidad_nueva)
                        carrito.monto_total -= cantidad_devolucion * producto_encontrado.precio
                        print(f'Se devolvieron {cantidad_devolucion} unidad(es) de {producto_encontrado.nombre} al stock.')
                        print('==' * 45)
                    elif cantidad_nueva > cantidad:
                        cantidad_a_agregar = cantidad_nueva - cantidad
                        if producto_encontrado.verificar_stock(cantidad_a_agregar):
                            producto_encontrado.modificar_stock(cantidad_a_agregar)
                            carrito.productos[index_producto] = (producto_encontrado, cantidad_nueva)
                            carrito.monto_total += cantidad_a_agregar * producto_encontrado.precio
                            print(f'Se agregaron {cantidad_a_agregar} unidad(es) de {producto_encontrado.nombre} al carrito.')
                            print('==' * 45)
                        else:
                            print(f'No hay suficiente stock de {producto_encontrado.nombre} para la cantidad deseada.')
                            print('==' * 45)
                    else:
                        print(f'No se realizaron modificaciones en la cantidad de {producto_encontrado.nombre}.')
                        print('==' * 45)
                else:
                    print('Producto no encontrado')
                    print('==' * 45)
            else:
                print('No se realizarán modificaciones en el carrito.')
                print('==' * 45)
        except ValueError:
            print('No ingresaste una opción válida, intenta nuevamente')
        else:
            break


