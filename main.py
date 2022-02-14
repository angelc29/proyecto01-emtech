from lifestore_file import lifestore_searches, lifestore_sales, lifestore_products
from datetime import datetime as dt
#import funciones #De esta manera hay que anteponer 'funciones' antes de usar cada una
from funciones import *
"""
La info de lifestore_file:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

"""
Login
credenciales:

usuario:
    angelC
contrasenia:
    admindb321
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
    if usuario == 'angelC' and contras == 'admindb321':
        usuarioAccedio = True
        print('\nHola de nuevo',usuario,'!')
    else:
        print(f'Tienes {3 - intentos} intentos restantes')
        if usuario == 'angel':
            print('Te equivocaste en la contraseña')
        else:
            print(f'El usuario: "{usuario}" no esta registrado')           
        
        if intentos == 3:
            exit()

# Ejecuta la funcion principal para contar las ventas
ventas = ventasSorted()
sinVentas = [venta for venta in ventas if venta[5]==0]  
# Ejecuta la funcion principal para contar las busquedas
busquedas=busquedasSorted()
sinBusquedas = [bus for bus in busquedas if bus[5] == 0]
#Se obtiene una lista de productos con su correspondiente reseña general
resProductos = reseniasProds()

def printMenu():
    print("\n")
    print('Menu principal')
    print(' 1. Consultar los 5 productos más vendidos')
    print(' 2. Consultar los 10 productos más buscados')
    print(' 3. Ver los productos menos vendidos por categoria')
    print(' 4. Ver los productos menos buscados por categoria')
    print(' 5. Consultar los productos con peor y mejor reseña')  
    print(' 6. Ver el informe de ventas')
    print(' 7. Estrategia Sugerida')
    print(' 0. Salir')

# Menu principal
printMenu()
menuMain = int(input("Ingresa una opción: "))
while menuMain !=0:
    if menuMain == 1:
        # Resuelve el punto 1.1 del PUNTO 1
        # Realiza un calculo del numero de ventas total sin considerar devoluciones
        totalSales = 0
        for ven in ventas:
            totalSales+=ven[5]
        print("\nHubo un total de",totalSales,"ventas satisfactorias")
        print("\nTop de los 5 productos más vendidos")       
        # Se ordena de acuerdo al numero de ventas de cada producto (mayor a menor)
        ventas = sortList(ventas,5,True)
        for i,v in enumerate(ventas[:5],start=1):
            print(f"    {i}.- Las ventas del producto {v[1]} fueron {v[5]}")        
    elif menuMain == 2:
        # Resuelve el punto 1.2 del PUNTO 1
        print("\nHubo un total de",len(lifestore_searches),"busquedas")
        print("\nTop de los 10 productos más buscados")     
        # Se ordena la lista de mayor a menor segun su numero de busquedas
        busquedas=sortList(busquedas,5,True)
        for i,s in enumerate(busquedas[:10],start=1):
            print(f"    {i}.- Las busquedas del producto {s[1]} fueron {s[5]}")
    elif menuMain == 3:
        # # Se resuelve el punto 2.1 del PUNTO 1
        # Se ordenan las ventas
        ventas = sortList(ventas,5,True)
        # Con la informacion de ventas se obtiene un diccionario que corresponde al tipo {categoria1: [venta1,venta2...], categoria2: [venta1,venta2...]...}            
        categorias = categorizar(ventas)
        print("\nProductos menos vendidos de",len(categorias),"categorias (mostrando hasta 5):\n")
        # Usa la funcion para limpiar de productos sin ventas
        categorias=limpiarCeros(categorias,5)            
        # Se limpia el diccionario para dejar solo 5 productos por categoria y con menos ventas
        menosVendidos = {cat:list(reversed(categorias[cat]))[:5] for cat in categorias}
        # Se muestran hasta los 5 productos menos vendidos por categoria
        for cat in menosVendidos:
            print(f"Menos vendidos de la categoria {cat}:")
            for i,v in enumerate(menosVendidos[cat],start=1):
                print(f"    {i}.- {v[1]} ----------- {v[5]} ventas")
    elif menuMain == 4:
        # # Se resuelve el punto 2.2 del PUNTO 1
        # Se ordenan las busquedas
        busquedas=sortList(busquedas,5,True)
        # Con la informacion de busquedas se obtiene un diccionario parecido al que se genero anteriormente
        categorias = categorizar(busquedas)
        print("\nProductos menos buscados de",len(categorias),"categorias (mostrando hasta 10):\n")
        # Se limpian los renglones de productos que no tuvieron busquedas
        categorias=limpiarCeros(categorias,5)       
        # Se guarda una nueva lista con al menos 10 productos con menores busquedas por categoria 
        menosBuscados = {cat:list(reversed(categorias[cat]))[:10] for cat in categorias}
        # Se muestran los productos con menores busquedas por categoria
        for cat in menosBuscados:
            if len(menosBuscados[cat]) != 0:
                print(f"Menos buscados de la categoria {cat}:")
                for i,b in enumerate(menosBuscados[cat],start=1):
                    print(f"    {i}.- {b[1] } ----------- {b[5]} busquedas")
            else:
                print("Sin busquedas para la categoria",cat)      
    elif menuMain == 5:
        # # Resuelve el PUNTO 2 
        # Elimina los producto que no obtuvieron reseñas generales por no tener ninguna venta y devuelve esta lista limpia
        resProductosCpy = [p_res for p_res in resProductos if p_res[5]!=0]      
        print("\nLa cantidad de productos reseñados fue de",len(resProductosCpy))
        # Se ordena la lista con reseñas de acuerdo a esta de mayor a menor
        resProductosCpy = sortList(resProductosCpy,5,True)
        print("\nTop 5 mejores productos de acuerdo a su reseña")
        # Se muestran los 5 productos con mejor reseña
        for i,p_res in enumerate(resProductosCpy[:5],start=1):
            print(f"    {i}.- {p_res[1]} tiene una reseña de {p_res[5]}")
        print("Top 5 peores productos de acuerdo a su reseña")
        # Se muestran los 5 productos con peor reseña
        for i,p_res in enumerate(list(reversed(resProductosCpy))[:5],start=1):
            print(f"    {i}.- {p_res[1]} tiene una reseña de {p_res[5]}")
    elif menuMain == 6:
        # Resuelve el PUNTO 3
        print("\nInforme general de las ventas de LifeStore\n")
        # La funcion ventasMeses obtiene un diccionario donde estan agrupadas las ventas por mes y se ordena con la funcion ordenaMeses
        ventas_meses = ordenaMeses(ventasMeses())
        # Se crea una lista para contener los ingresos mensuales
        ingresos_meses=[]
        cantVentas_meses = []
        print('Ingresos Mensuales\n')
        for mes in dict_meses:
            totalMensual = 0
            notVentas = False
            try:
                for venta in ventas_meses[mes]:
                    totalMensual+=venta[5]
                if totalMensual == 0:
                    notVentas = True
                    print('    Hubo devoluciones.',end=' ')
            except:
                notVentas = True
            if notVentas:
                print('    El mes',mes,'no tuvo ventas')
                cantVentas_meses.append(0)
            else:
                print(f'    {mes} generó {totalMensual}.00 MXN de ingresos y hubo {len(ventas_meses[mes])} ventas')
                cantVentas_meses.append(len(ventas_meses[mes]))
            ingresos_meses.append(totalMensual)   

        # Se obtiene el promedio de ingresos mensuales
        promMensual=sum(ingresos_meses)/len(ingresos_meses) #Considerando 12 meses
        print('\nEl promedio general de ingresos de ventas mensuales fue de',promMensual,'MXN')
        print('\nEl total de ingresos generados en 2020 fué de',sum(ingresos_meses),'.00 MXN')
        print('\nMeses con mas ventas')
        cantVentas_meses = {key : cantVentas_meses[idx] for idx,key in enumerate(dict_meses)}
        for i,it in enumerate(sorted(cantVentas_meses.items(),key=lambda x: x[1],reverse=True)[:5],start=1):
            print(f'    {i}.- {it[0]} tuvo {it[1]} ventas')
    elif menuMain == 7:
        # Se realiza una interseccion entre productos sin ventas y sin busquedas para saber que productos estan mas olvidados
        rezagados = [prod for prod in sinVentas if prod in sinBusquedas]
        # Se ordenan de acuerdo a su stock
        rezagados = sortList(rezagados,4,True)
        print('\nHay un total de',len(rezagados),'productos sin busquedas y sin ventas')
        print('\nLa sugerencia es promocionar, rematar y por consiguiente liberar el espacio que ocupan estos productos rezagados, comenzando con los que mayor stock tienen\n')
        for i,r in enumerate(rezagados,start=1):
            print(f'  {i}.- {r[1]}\n        Categoría: {r[3]}\n        Existencias: {r[4]}')
    else:
        print('Ingrese una opción valida')
    input('\nEsperando Enter para continuar...')
    printMenu()
    menuMain = int(input("Ingresa una opción: "))   

# ob_datetime = datetime.strptime("21/05/2020",formato)
# print("fecha:",ob_datetime.strftime(formato))

# #Ejemplo de comprension de listas
# pares = [par for par in 
#             [num**2 for num in range(0,11)] 
#                 if par%2==0]
# print(pares)
