import requests
import lxml.html as html    #para xpath
import os                   #para crear carpetas
import datetime             #manejo de fechas

XPATH_PRODUCT_DESCRIPTION = '//h1/span/text()'
XPATH_PRODUCT_PRICE_INTEGER = '//span[@class="vtex-product-price-1-x-currencyContainer vtex-product-price-1-x-currencyContainer--shelf-main-selling-price"]/span[@class="vtex-product-price-1-x-currencyInteger vtex-product-price-1-x-currencyInteger--shelf-main-selling-price"]/text()'
XPATH_PRODUCT_PRICE_DECIMAL = '//span[@class="vtex-product-price-1-x-currencyContainer vtex-product-price-1-x-currencyContainer--shelf-main-selling-price"]/span[@class="vtex-product-price-1-x-currencyFraction vtex-product-price-1-x-currencyFraction--shelf-main-selling-price"]/text()'

def parsearUnProducto(link, contador):
    try:
        #print(f'El link es: {link}')
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
                print ('\n')
                print(f'La descripción del producto {contador} es: {descripcion}')
                precioEntero = parsed.xpath(XPATH_PRODUCT_PRICE_INTEGER)[0]
                print(f'El precio (parte entera) es: {precioEntero}')
                precioDecimal = parsed.xpath(XPATH_PRODUCT_PRICE_DECIMAL)[0]
                print(f'El precio (parte decimal) es: {precioDecimal}')
                today = datetime.date.today().strftime('%d-%m-%Y')
                #print(listadoProductos)
                if not os.path.isdir(today):
                    os.mkdir(today)
                with open(f'{today}/Vea.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{descripcion}: ${precioEntero},{precioDecimal} \n')
            except  IndexError as ie:
                print('\n')
                print(f'No se pudo leer el artículo {contador}. Probable problema de xpath ó conexión. El error es: {ie}')
        else:
            #raise ValueError(f'Error: {response.status_code}')
            print(f'Error de comunicación. El código de retorno es {response.status_code}')
    except ValueError as ve:
        print(f'El error: {ve}')