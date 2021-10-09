import requests
import lxml.html as html    #para xpath
import os                   #para crear carpetas
import datetime             #manejo de fechas
import time

XPATH_PRODUCT_DESCRIPTION = '//h1[@class="product_page" and contains(@style,"font")]/text()'
XPATH_PRODUCT_PRICE = '//div[@class="price_regular_container"]//span[@class="price_regular_precio"]/text()'

def parsearUnProducto(link, contador):
    try:
        print(f'El link es: {link}')
        response = requests.get(link)
        if response.status_code == 200:
            producto = response.content.decode('utf-8')
            producto = producto.replace('\"', '')
            """
            with open ('noticiasPpales.txt', 'w') as file:
                sys.stdout = file
                print(notice)
                sys.stdout = original_stdout
            """
            #with open(f'CotoLecheDetalle.txt', 'w', encoding='utf-8') as f:
            #    f.write(producto)
            #    f.write('\n\n')
            parsed = html.fromstring(producto)
            try:
                descripcion = parsed.xpath(XPATH_PRODUCT_DESCRIPTION)[0]
                descripcion = descripcion.strip()
                #descripcion = descripcion.replace('\"', '')
                #print ('\n')
                print(f'La descripción del producto {contador} es: {descripcion}')
                time.sleep(2)
                precio = parsed.xpath(XPATH_PRODUCT_PRICE)[0]
                print(f'El precio es: {precio}')
                today = datetime.date.today().strftime('%d-%m-%Y')
                #print(listadoProductos)
                if not os.path.isdir(today):
                    os.mkdir(today)
                #with open(f'{today}/Dia.txt', 'a', encoding='utf-8') as f:
                #    f.write(f'{descripcion}: ${precio} \n')
            except  IndexError as ie:
                print('\n')
                print(f'No se pudo leer completo el artículo {contador}. Probable problema de conexión. El error es: {ie}')
            except Exception as e:
                print('\n')
                print(f'error: {e}')
        else:
            #raise ValueError(f'Error: {response.status_code}')
            print(f'Error de comunicación. El código de retorno es {response.status_code}')
    except ValueError as ve:
        print(f'El error: {ve}')