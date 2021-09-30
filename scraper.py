import requests
import lxml.html as html    #para xpath
import sys
import os                   #para crear carpetas
import datetime             #manejo de fechas
import parseProductosPorTipo

original_stdout = sys.stdout

#supermercado Vea, categorias
listaUrlsProductos = ['https://www.vea.com.ar/leche?map=ft', 'https://www.vea.com.ar/yerba?map=ft', 'https://www.vea.com.ar/azucar?map=ft']

XPATH_HOW_MANY_PRODUCTS = '//div[@class="vtex-search-result-3-x-totalProducts--layout pv5 ph9 bn-ns bt-s b--muted-5 tc-s tl t-action--small"]/span/text()'

XPATH_PRODUCT_DESCRIPTION = '//h1[@class="vtex-store-components-3-x-productNameContainer mv0 t-heading-4"]/span[@class="vtex-store-components-3-x-productBrand "]/text()'
XPATH_PRODUCT_PRICE_INTEGER = '//span[@class="vtex-product-price-1-x-currencyContainer vtex-product-price-1-x-currencyContainer--shelf-main-selling-price"]/span[@class="vtex-product-price-1-x-currencyInteger vtex-product-price-1-x-currencyInteger--shelf-main-selling-price"]/text()'
XPATH_PRODUCT_PRICE_DECIMAL = '//span[@class="vtex-product-price-1-x-currencyContainer vtex-product-price-1-x-currencyContainer--shelf-main-selling-price"]/span[@class="vtex-product-price-1-x-currencyFraction vtex-product-price-1-x-currencyFraction--shelf-main-selling-price"]/text()'


def parse_products(link, today, contador):
    try:
        print(f'El link es: {link}')
        response = requests.get(link)
        if response.status_code == 200:
            producto = response.content.decode('utf-8')
            #producto = producto.replace('\"', '')
            """
            with open ('noticiasPpales.txt', 'w') as file:
                sys.stdout = file
                print(notice)
                sys.stdout = original_stdout
            """
            #with open(f'VeaLechesDetalle.txt', 'w', encoding='utf-8') as f:
            #    f.write(producto)
            #    f.write('\n\n')
            parsed = html.fromstring(producto)
            try:
                descripcion = parsed.xpath(XPATH_PRODUCT_DESCRIPTION)[0]
                #descripcion = descripcion.replace('\"', '')
                print ('\n\n')
                print(f'La descripción del producto {contador} es: {descripcion}')
                precioEntero = parsed.xpath(XPATH_PRODUCT_PRICE_INTEGER)[0]
                print(f'El precio (parte entera) es: {precioEntero}')
                precioDecimal = parsed.xpath(XPATH_PRODUCT_PRICE_DECIMAL)[0]
                print(f'El precio (parte decimal) es: {precioDecimal}')
                with open(f'{today}/Vea.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{descripcion}: ${precioEntero},{precioDecimal} \n')
            except  IndexError as ie:
                print(f'El error es: {ie}')
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(f'El error: {ve}')

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
                parse_products(link, today, contador)
                contador = contador + 1
        else:
            raise ValueError(f'Error')
    except ValueError as ve:
        print(ve)


