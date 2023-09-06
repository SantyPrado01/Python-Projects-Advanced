import sqlite3

basededatos = sqlite3.connect('prueba.bd')

basededatos.execute('''
    select b.codbarrio, b.nombre, c.nombre 
    from ciudad c inner join
    barrio b 
    on c.codciudad = b.codciudad 
''')# Se unen mediante la realcion calve primaria y clave foreana, asi traremos todas la relaciones de la tabla


#De forma opcional podemos usar un where para traer lo que necesitamos:
basededatos.execute('''
    select b.codbarrio, b.nombre, c.nombre 
    from ciudad c inner join
    barrio b 
    on c.codciudad = b.codciudad 
    where c.codciudad = 1 
''')
#Asi solamente se traeria los barrios que esten relacionados con la ciudad uno





basededatos.execute('''
    from cliente c inner join venta v on c.codcliente = v.codcliente
                    where c.codcliente = 1 
                    and v.fecha >= '01-08-2023'
                    and v.fecha <= '31-08-2023'


''')
                    

     