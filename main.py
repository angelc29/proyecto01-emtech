from lifestore_file import lifestore_searches, lifestore_sales, lifestore_products
"""
La info de lifestore_file:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

# # # PUNTO 1 # # #
# -> Toda lista generada con resultados puede ser añadida a la lista de products o una copia
# 1.1 Generar listado de 5 productos con mayores ventas 
#       Obtener la cantidad de ventas(sales) de 1 producto
#       Obtener una lista con la cantidad de ventas de todos los productos
#       Ordenar esa lista de mayor a menor y obtener los nombres de 5 productos    
# 1.2 Generar listado de 5 productos con mayores busquedas
#       Obtener la cantidad de busquedas(searches) de 1 producto
#       Obtener la cantidad de busquedas de todos los productos 
#       Ordenar esa lista de mayor a menor y capturar los 10 primeros productos
#
# 2.1 Generar listado con los 5 productos con menores ventas, esto por categoria
#       Usar los resultados de 1.1
#       Generar clusteres por categoria
#       Ordenar cada cluster de mayor a menor de acuerdo a las ventas(n sales) 
#       Mostrar los ultimos 5 productos de cada cluster        
# 2.2 Generar listado con los 10 productos con menores busquedas, esto por categoria
#       Usar los resultados de 1.2
#       Generar clusteres por categoria
#       Ordenar cada cluster de mayor a menor de acuerdo a las busquedas(n searches)
#       Mostrar los ultimos 10 productos de cada cluster    
#   *Probablemente no se alcance el numero solicitado de productos a mostrar en los puntos de 2.x 

# Resuelve el punto 1.1
def ventasTop5():
    # Una copia de los productos para concatenar como columna al numero de ventas
    ventas = lifestore_products.copy()
    # Recorre la lista de productos
    for i,product in enumerate(lifestore_products):
        # Obtiene id de un producto y se crea la variable para sumar sus ventas
        id_prod=product[0]      
        numVentas = 0
        # Se recorren las ventas buscando al producto en cuestion y se suma el numero de apariciones
        for sale in lifestore_sales:
            if id_prod == sale[1]:
                numVentas+=1
        # Se concatena el numero de ventas con el producto analizado
        ventas[i].append(numVentas)
    # Se ordena de acuerdo al numero de ventas que tuvo cada producto
    ventas=sorted(ventas,reverse=True, key=lambda x:x[5])
    # Imprime los 5 productos con mas ventas (apariciones en lista de ventas)
    return ventas[:5] 

cincoVentas = ventasTop5()
for v in cincoVentas:
        print(f"Las ventas del producto {v[1]} fueron {v[5]}")

# # # PUNTO 2 # # #
# 1. Generar 2 listados de 5 productos con las mejores y peores reseñas
#   *Considerar productos con devolucion
#   *No considerar productos con 0 de reseña
#       Obtener la reseña de 1 producto
#           Se capturan las ventas de 1 producto
#               De la lista de ventas se obtiene cada ventas de acuerdo a la id del producto   
#           Se obtienen las reseñas de estas ventas
#           Se obtiene un promedio
#       Obtener la reseña de todos los productos iterando la funcion que obtiene la reseña general            
#       Generar lista de reseñas de todos productos
#       Ordenar de mayor a menor a los productos de acuerdo a su reseña general
#       Mostrar los primeros 5 y los ultimos 5

# # # PUNTO 3 # # #
# # *Filtrar ventas que se devolvieron y no considerarlas
# # *Al parecer no hay datos que sean de un año distinto a 2020
# 1.1 Calcular total de ingresos mensuales
#       Generar clusteres de la lista de ventas segun el mes
#       Añadir precios de acuerdo a la id del producto en los clusteres generados
#       Calcular el total de ingresos en cada cluster/mes
# 1.2 Calcular ventas promedio mensuales
#       Usar datos agrupados por mes de 1.1 
#       Contar el numero de ventas de cada mes/cluster
#       Obtener un promedio general de ventas    
# 1.3 Calcular ventas totales anuales
#       Usar datos agrupados por mes de 1.1 con precios
#       Calcular el total de ingresos de las ventas
# 1.4 Calcular meses con mas ventas
#       Usar datos de 1.2
#       Ordenar meses de mayor a menor
#       Mostrar numero de ventas por mes

# # Imprimir los primeros 10 prod.
# lista_diez = lifestore_products[:10]
# for producto in lista_diez:
#     print(producto[2], '\n')

# # Muestra los nombres de los primeros 10 productos
# names = [row[1][:10] for row in lifestore_products]
# for name in names:
#     print(name)

# #Ejemplo de comprension de listas
# pares = [par for par in 
#             [num**2 for num in range(0,11)] 
#                 if par%2==0]
# print(pares)

# # sumatoria de los precios los primeros 10 prod.
# suma = 0
# for producto in lista_diez:
#     # Obtener el precio del producto
#     precio = producto[2]
#     suma += precio

# print('El valor de la suma de los primeros 10 prod: ', suma)
# print('El valor promedio de los primeros 10 prod: ', suma/10)

"""
Login
credenciales:

usuario:
    angel
contrasenia:
    admin123
"""




"""

usuarioAccedio = False
intentos = 0

# Bienvenida!
mensaje_bienvenida = 'Bienvenido al sistema!\nAccede con tus credenciales'
print(mensaje_bienvenida)

# Recibo constantemente sus intentos
while not usuarioAccedio:
    # Primero ingresa Credenciales
    usuario = input('Usuario: ')
    contras = input('Contraseña: ')
    intentos += 1
    # Reviso si el par coincide
    if usuario == 'angel' and contras == 'admin123':
        usuarioAccedio = True
        print('Hola de nuevo!')
    else:
        # print('Tienes', 3 - intentos, 'intentos restantes')
        print(f'Tienes {3 - intentos} intentos restantes')
        if usuario == 'angel':
            print('Te equivocaste en la contraseña')
        else:
            print(f'El usuario: "{usuario}" no esta registrado')
            
    if intentos == 3:
        exit()

print('Solamente llegaste aca si ingresaste correctamente')

"""

