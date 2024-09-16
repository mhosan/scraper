import parseProductos
import parseProducto

listaUrlsProductos=[
'https://diaonline.supermercadosdia.com.ar/busca/?ft=leche',
'https://diaonline.supermercadosdia.com.ar/busca/?ft=yerba',
'https://diaonline.supermercadosdia.com.ar/busca/?ft=azucar',
'https://diaonline.supermercadosdia.com.ar/busca/?ft=galletitas',
'https://diaonline.supermercadosdia.com.ar/busca/?ft=gaseosas',
'https://diaonline.supermercadosdia.com.ar/busca/?ft=arroz',
'https://diaonline.supermercadosdia.com.ar/busca/?ft=shampoo',
'https://diaonline.supermercadosdia.com.ar/busca/?ft=pollo'
]
listaUrlsProductosTest=['https://diaonline.supermercadosdia.com.ar/busca/?ft=leche']

def procesarLista():
    contador = 1
    for urlProducto in listaUrlsProductos:
        try:
            listadoProductos = parseProductos.parseProductos(urlProducto, "Dia")
            #print('que corno me devuelve la sub:')
            #print(listadoProductos)
            if type(listadoProductos is list and len(listadoProductos) > 0) :
                for link in listadoProductos:
                    parseProducto.parseUnProducto(link, contador, "Dia")
                    contador = contador + 1
            else:
                raise ValueError(f'Error en la lista de productdos a parsear')
        except ValueError as ve:
            print(ve)

if __name__=='main':
    procesarLista()