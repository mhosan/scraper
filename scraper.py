import lxml.html as html    #para xpath
import parseProductosPorTipo
import parseUnproducto

#supermercado Vea, categorias
listaUrlsProductos = ['https://www.vea.com.ar/leche?map=ft', 'https://www.vea.com.ar/yerba?map=ft', 'https://www.vea.com.ar/azucar?map=ft']

for urlProducto in listaUrlsProductos:
    try:
        listadoProductos = parseProductosPorTipo.parseTipoProducto(urlProducto)
        if type(listadoProductos is list) :
            for link in listadoProductos:
                link = 'https://www.vea.com.ar' + link 
                parseUnproducto.parsearUnProducto(link, contador)
                contador = contador + 1
        else:
            raise ValueError(f'Error')
    except ValueError as ve:
        print(ve)


