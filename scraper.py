import lxml.html as html    #para xpath
import parseProductosPorTipo
import parseUnproducto

#supermercado Jumbo, categorias
listaUrlsProductos = ['https://www.jumbo.com.ar/busca/?ft=leche']

contador = 1
for urlProducto in listaUrlsProductos:
    try:
        listadoProductos = parseProductosPorTipo.parseTipoProducto(urlProducto)
        #print('que corno me devuelve la sub:')
        #print(listadoProductos)
        if type(listadoProductos is list and len(listadoProductos) > 0) :
            for link in listadoProductos:
                #link = 'https://www.vea.com.ar' + link 
                parseUnproducto.parsearUnProducto(link, contador)
                contador = contador + 1
        else:
            raise ValueError(f'Error en la lista de productdos a parsear')
    except ValueError as ve:
        print(ve)


