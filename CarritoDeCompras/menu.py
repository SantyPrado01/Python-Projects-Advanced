from funciones import *

print('=='*45)
print('Bienvenido a iTech')
print('=='*45)
print('Los productos que tenemos disponibles son: ')

for Producto in productos:
    print(Producto)
terminar = True
while terminar == True:
    carrito = CarritoCompras()
    print('Menu')
    print('Mostrar productos y sus detalles ----> Opcion 1 \nMostrar Informacion Breve Productos ----> Opcion 2 \nBuscar Productos por codigo ----> Opcion 3 \nRealizar Compra ---> Opcion 4 \nFinalizar Compra ---> Opcion 5 \nSalir ---> Opcion 6')
    
    try:
        
        opcion = int(input('Ingresar opcion: '))
        
        if opcion == 1:
        
            print('Opcion 1')
            
            opcion_uno()
            
        elif opcion == 2:
        
            print('Opcion 2')
            
            opcion_dos()
            
        elif opcion == 3:
            
            opcion_tres()
        
        elif opcion == 4:
            
            opcion_cuatro()
            
            
        elif opcion == 5:
            print('Finalizar Compra')
            opcion_cinco()
            
        
        elif opcion == 6:
            print('Salir del Sistema')
            terminar = False
                        
        else:
            print('Nada ingresado')
        continue
    except ValueError:
        print('Ingresa una opcion valida')
        continue  
    else:
        break       
    
 


