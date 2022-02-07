from lifestore_file import lifestore_searches, lifestore_sales, lifestore_products
import statistics as st
import numpy as np
import matplotlib.pyplot as plt
"""
La info de lifestore_file:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

# data = np.array(lifestore_sales)
# hist,bin_edges = np.histogram(data,10)
# plt.hist(data,bins=bin_edges)
# plt.show()

# # Imprimir los primeros 10 prod.
# lista_diez = lifestore_products[:10]
# for producto in lista_diez:
#     print(producto[2], '\n')

names = [row[1][:10] for row in lifestore_products]

for name in names:
    print(name)

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

