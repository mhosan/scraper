import lxml.html as html    #para xpath
import parseProductosPorTipo
import parseUnproducto

#supermercado Vea, categorias
listaUrlsProductosOriginal=[
'https://diaonline.supermercadosdia.com.ar/busca/?ft=leche',
'https://diaonline.supermercadosdia.com.ar/busca/?ft=yerba',
'https://diaonline.supermercadosdia.com.ar/busca/?ft=azucar',
'https://diaonline.supermercadosdia.com.ar/busca/?ft=galletitas',
'https://diaonline.supermercadosdia.com.ar/busca/?ft=gaseosas',
'https://diaonline.supermercadosdia.com.ar/busca/?ft=arroz',
'https://diaonline.supermercadosdia.com.ar/busca/?ft=shampoo',
'https://diaonline.supermercadosdia.com.ar/busca/?ft=pollo']
listaUrlsProductos=['https://maxiconsumo.com/sucursal_capital/catalogsearch/result/?q=leche']
contador = 1
for urlProducto in listaUrlsProductos:
    try:
        listadoProductos = parseProductosPorTipo.parseTipoProducto(urlProducto)
        #print('que corno me devuelve la sub:')
        #print(listadoProductos)
        if type(listadoProductos is list and len(listadoProductos) > 0) :
            for link in listadoProductos:
                parseUnproducto.parsearUnProducto(link, contador)
                contador = contador + 1
        else:
            raise ValueError(f'Error en la lista de productdos a parsear')
    except ValueError as ve:
        print(ve)


