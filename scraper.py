import requests
import lxml.html as html    #para xpath
import sys
import os                   #para crear carpetas
import datetime             #manejo de fechas

original_stdout = sys.stdout

#supermercado Vea, categoria: Leche
HOME_URL = 'https://www.vea.com.ar/leche?map=ft'
XPATH_HOW_MANY_PRODUCTS = '//div[@class="vtex-search-result-3-x-totalProducts--layout pv5 ph9 bn-ns bt-s b--muted-5 tc-s tl t-action--small"]/span/text()'
XPATH_PRODUCTS_LIST = '//section[@class="vtex-product-summary-2-x-container vtex-product-summary-2-x-containerNormal overflow-hidden br3 h-100 w-100 flex flex-column justify-between center tc" and @style="max-width:300px"]//a/@href'
XPATH_PRODUCT_DESCRIPTION = '//h1[@class="vtex-store-components-3-x-productNameContainer mv0 t-heading-4"]/span[@class="vtex-store-components-3-x-productBrand "]/text()'
XPATH_PRODUCT_PRICE_INTEGER = '//span[@class="vtex-product-price-1-x-currencyContainer vtex-product-price-1-x-currencyContainer--shelf-main-selling-price"]/span[@class="vtex-product-price-1-x-currencyInteger vtex-product-price-1-x-currencyInteger--shelf-main-selling-price"]/text()'
XPATH_PRODUCT_PRICE_DECIMAL = '//span[@class="vtex-product-price-1-x-currencyContainer vtex-product-price-1-x-currencyContainer--shelf-main-selling-price"]/span[@class="vtex-product-price-1-x-currencyFraction vtex-product-price-1-x-currencyFraction--shelf-main-selling-price"]/text()'

#
#XPATH_LINK_TO_ARTICLE_MAIN = '//article[@class="content-nota list-format twoxone_no_foto"]/a[@class="link_article"]/@href'
#XPATH_LINK_TO_ARTICLE_SECONDARY = '//article[@class="content-nota list-format onexone_no_foto no-p"]/a[@class="link_article"]/@href'
#XPATH_LINK_TO_ARTICLE_SECONDARY_FOTO = '//article[@class="content-nota onexone_foto    list-format flex-change"]/a[@class="link_article"]/@href'

#titulos de las notas del los titulares
#XPATH_TITLE_MAIN = '//div[@class="title"]/h1[@id="title"]/text()'

#resumen de las notas principales o titulares
#XPATH_SUMMARY_MAIN = '//div[@class="bajada"]/h2/text()'

#cuerpo de la noticia principal
#XPATH_BODY_MAIN = '//div[@class="body-nota"]/p/text()'


def parse_products(link, today, contador):
    try:
        #print ('\n\n')
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
                print ('\n\n')
                print(f'La descripción del producto {contador} es: {descripcion}')
                precioEntero = parsed.xpath(XPATH_PRODUCT_PRICE_INTEGER)[0]
                print(f'El precio (parte entera) es: {precioEntero}')
                precioDecimal = parsed.xpath(XPATH_PRODUCT_PRICE_DECIMAL)[0]
                print(f'El precio (parte decimal) es: {precioDecimal}')
            except  IndexError as ie:
                print(f'El error es: {ie}')
            with open(f'{today}/Vea.txt', 'a', encoding='utf-8') as f:
                f.write(f'{descripcion}: ${precioEntero},{precioDecimal} \n')
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(f'El error: {ve}')


try:
    response = requests.get(HOME_URL)
    if response.status_code == 200:
        home = response.content.decode('utf-8', errors='replace')
        """
        with open ('vea.txt', 'w') as f:
            sys.stdout = f
            print(home)
            sys.stdout = original_stdout

        with open(f'paginaVeaLeche.txt', 'w', encoding='utf-8') as f:
                f.write(home)
                f.write('\n\n')
        """
        parsed = html.fromstring(home)
        totalProductos = parsed.xpath(XPATH_HOW_MANY_PRODUCTS)[0]
        print (f'Total de productos: {totalProductos}')
        print ('\n')
        listadoProductos= parsed.xpath(XPATH_PRODUCTS_LIST)
        print(listadoProductos)
        print (f'La lista de productos tiene {len(listadoProductos)} elementos.')
        today = datetime.date.today().strftime('%d-%m-%Y')
        if not os.path.isdir(today):
            os.mkdir(today)
        contador = 0
        for link in listadoProductos:
            link = 'https://www.vea.com.ar' + link 
            parse_products(link, today, contador)
            contador = contador + 1
    else:
        raise ValueError(f'Error: {response.status_code}')
except ValueError as ve:
    print(ve)

