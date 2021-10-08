import requests
import lxml.html as html    #para xpath
import os                   #para crear carpetas
import datetime             #manejo de fechas

XPATH_PRODUCT_DESCRIPTION = '//div[@class="info-wrapper"]/h1[@class="name"]/div//text()'
XPATH_PRODUCT_PRICE = '//em[@class="valor-por"]/strong//text()'

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
                precio = parsed.xpath(XPATH_PRODUCT_PRICE)[0]
                print(f'El precio es: {precio}')
                today = datetime.date.today().strftime('%d-%m-%Y')
                #print(listadoProductos)
                if not os.path.isdir(today):
                    os.mkdir(today)
                with open(f'{today}/Jumbo.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{descripcion}: ${precio} \n')
            except  IndexError as ie:
                print('\n')
                print(f'No se pudo leer el artículo {contador}. Probable problema de conexión. El error es: {ie}')
        else:
            #raise ValueError(f'Error: {response.status_code}')
            print(f'Error de comunicación. El código de retorno es {response.status_code}')
    except ValueError as ve:
        print(f'El error: {ve}')