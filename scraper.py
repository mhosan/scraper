import requests
import lxml.html as html    #para xpath
import sys
import os                   #para crear carpetas
import datetime             #manejo de fechas
import parseProductosPorTipo
import parseUnproducto

original_stdout = sys.stdout

#supermercado Vea, categorias
listaUrlsProductos = ['https://www.vea.com.ar/leche?map=ft', 'https://www.vea.com.ar/yerba?map=ft', 'https://www.vea.com.ar/azucar?map=ft']

for urlProducto in listaUrlsProductos:
    try:
        listadoProductos = parseProductosPorTipo.parseTipoProducto(urlProducto)
        if type(listadoProductos is list) :
            today = datetime.date.today().strftime('%d-%m-%Y')
            #print(listadoProductos)
            if not os.path.isdir(today):
                os.mkdir(today)
                contador = 1
            for link in listadoProductos:
                link = 'https://www.vea.com.ar' + link 
                parseUnproducto.parsearUnProducto(link, today, contador)
                contador = contador + 1
        else:
            raise ValueError(f'Error')
    except ValueError as ve:
        print(ve)


