import parseProductos
import parseProducto


listaUrlsProductos = [
'https://www.vea.com.ar/leche?map=ft',
'https://www.vea.com.ar/yerba?map=ft', 
'https://www.vea.com.ar/azucar?map=ft',
'https://www.vea.com.ar/galletitas?map=ft',
'https://www.vea.com.ar/gaseosas?map=ft',
'https://www.vea.com.ar/arroz?map=ft',
'https://www.vea.com.ar/shampoo?map=ft',
'https://www.vea.com.ar/pollo?map=ft'
]
listaUrlsProductosTest=[
'https://www.vea.com.ar/leche?map=ft',
'https://www.vea.com.ar/azucar?map=ft'
]
def procesarLista():
    contador = 1
    for urlProducto in listaUrlsProductos:
        try:
            listadoProductos = parseProductos.parseProductos(urlProducto, "Vea")
            #print('que corno me devuelve la sub:')
            #print(listadoProductos)
            if type(listadoProductos is list and len(listadoProductos) > 0) :
                for link in listadoProductos:
                    link = 'https://www.vea.com.ar' + link 
                    parseProducto.parseUnProducto(link, contador, "Vea")
                    contador = contador + 1
            else:
                raise ValueError(f'Error en la lista de productdos a parsear')
        except ValueError as ve:
            print(ve)

