from lifestore_file import lifestore_searches, lifestore_sales, lifestore_products
from datetime import datetime as dt

# Ordena y devuelve una lista de listas l de acuerdo a un parametro en la posicion i 
def sortList(l,i,h_to_l):
    return sorted(l,reverse=h_to_l,key=lambda x:x[i])

# Funcion para mostrar el diccionario 
def showDict(dict):
    total=0
    for key in dict:
        total+=len(dict[key])
        print(key, f" {len(dict[key])} values")
        for value in dict[key]:
            print("     ",value)
    print("Total values:",total)

# Limpia un diccionario de tuplas con ceros en el lugar index
def limpiarCeros(dict,index):
    for key in dict:
        dict[key] = [v for v in dict[key] if v[index]!=0]
    return dict

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

# Obtiene el numero de busquedas por producto y concatena este valor en una copia de la lista productos
def busquedasSorted():
    # Una copia de la lista de productos para concatenarle el numero de busquedas, copia profunda
    busquedas = [row[:] for row in lifestore_products]
    # Recorre a la lista de productos y obtiene id_prod
    for i,product in enumerate(lifestore_products):
        id_prod = product[0]
        numBusq = 0
        # Recorre la lista de busquedas encontrando coincidencias con el producto en cuestion
        for search in lifestore_searches:
            if id_prod == search[1]:
                numBusq+=1
        # Se concatena el numero de busquedas con la informacion del producto
        busquedas[i].append(numBusq)
    # Devuelve la lista con busquedas
    return busquedas

# Obtiene el numero de ventas por producto y concatena este valor en una copia de la lista de productos
def ventasSorted():
    # Una copia de los productos para concatenar como columna al numero de ventas, copia profunda
    ventas = [row[:] for row in lifestore_products]
    # Recorre la lista de productos
    for i,product in enumerate(lifestore_products):
        # Obtiene id de un producto y se crea la variable para sumar sus ventas
        id_prod=product[0]      
        numVentas = 0
        
        # Se recorren las ventas buscando al producto en cuestion y se suma el numero de apariciones
        for sale in lifestore_sales:
            if id_prod == sale[1] and sale[4]==0:
                numVentas+=1
        # Se concatena el numero de ventas con el producto analizado
        ventas[i].append(numVentas)
    # Devuelve la lista con ventas
    return ventas

# Categoriza la lista de productos (utiliza el indice 3 para generar grupos) y regresa un diccionario 
def categorizar(lista_productos):
    # Se crea un diccionario para agrupar productos por categoria, en un inicio solo guardamos los nombres
    categorias = {}
    categorias = {prod[3] : [] for prod in lista_productos if prod[3] not in categorias}
    # Se rellena este diccionario con la informacion de la lista dada
    for prod in lista_productos:
        for cat in categorias.keys():
            # Se recorre sobre los productos y se van almacenando cada una de estos en el diccionario de categorias
            if prod[3] == cat:
                categorias[cat].append(prod)
    return categorias

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

# Obtiene una lista de productos con su correspondiente reseña concatenada como una columna
def reseniasProds():
    # Crea una copia de la lista principal de productos
    reseniasProds = [row[:] for row in lifestore_products]
    # Recorre la lista productos para obtener la id_prod y correr la funcion getResProm() por cada producto, 
    # despues almacena esta reseña general en la lista recien creada correspondiendo al producto
    for idx,prod in enumerate(lifestore_products):
        id_prod = prod[0]
        res = getResProm(id_prod)
        reseniasProds[idx].append(res)
    # Elimina los producto que no obtuvieron reseñas generales por no tener ninguna venta y devuelve esta lista limpia
    reseniasProds = [p_res for p_res in reseniasProds if p_res[5]!=0]
    return reseniasProds   

# Obtiene la reseña promedio de un solo producto dada su id_prod 
def getResProm(id_prod):
    # Crea una lista que almacena todas las reseñas del producto solicitado
    resenias = [v[2] for v in lifestore_sales if id_prod == v[1]]
    prom = sum(resenias)
    # Se obtiene un promedio de los numeros en la lista resenias 
    # y en caso de no tener reseñas/ventas no forzar una division entre 0
    if(prom != 0):
        prom = prom/len(resenias)
    # Finalmente se devuelve la reseña promedio redondeada a 2 decimales
    return round(prom,2)

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

# Formato correspondiente a las ventas de lifestore_sales
formato = "%d/%m/%Y"
# Se crea un diccionario del tipo mes : mes_numero que ayudará a ordenar el diccionario de ventas por meses
dict_meses={ "Enero" : 1, 
             "Febrero" : 2, 
             "Marzo" : 3,
             "Abril" : 4, 
             "Mayo" : 5, 
             "Junio" : 6,
             "Julio" : 7, 
             "Agosto" : 8, 
             "Septiembre" : 9 , 
             "Octubre" : 10,
             "Noviembre" : 11,
             "Diciembre" : 12
             }

# La siguiente funcion agrupa las ventas por meses en un diccionario
def ventasMeses():
    # Se genera una copia de lifestore_sales
    aux_ventas = [row[:] for row in lifestore_sales]
    # Se le concatena el precio de cada producto en las ventas
    for prod in lifestore_products:
        for idx,venta in enumerate(aux_ventas):
            if prod[0]==venta[1]:
                aux_ventas[idx].append(prod[2])

    # Crea un diccionario de ventas por meses de la forma {mesNum: [v1,v2,v3...], mesNum [v1,v2,v3...]...}
    ventas_meses = {dt.strptime(sale[3],formato).strftime("%m") : [] for sale in aux_ventas}

    # Se inserta cada una de las ventas en su correspondiente mes sin considerar a las devoluciones
    for mes in ventas_meses.keys():
        for sale in aux_ventas:
            if dt.strptime(sale[3],formato).strftime("%m") == mes and sale[4]==0:
                ventas_meses[mes].append(sale)
    return ventas_meses

# Esta funcion ordena el diccionario de ventas por meses
# Cambia la llave para identificarla por un string y los ordena como calendario            
def ordenaMeses(ventas_meses):
    # Crea una copia con las llaves del diccionario en numeros, se usará para ordenar estos y cambiarlos a cadenas
    aux_meses = list(ventas_meses.keys())
    # A continuacion se ordena el diccionario por meses y a su vez se convierte a cadena el numero de mes (llaves)
    for mesStr,mDig in dict_meses.items():
        for mes in aux_meses:
            if int(mes) == mDig:
                ventas_meses[mesStr] = ventas_meses[mes]
                del ventas_meses[mes]
                break
    return ventas_meses