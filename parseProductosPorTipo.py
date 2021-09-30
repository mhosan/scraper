import requests
import lxml.html as html    #para xpath

XPATH_PRODUCTS_LIST_LECHE = '//section[@class="vtex-product-summary-2-x-container vtex-product-summary-2-x-containerNormal overflow-hidden br3 h-100 w-100 flex flex-column justify-between center tc" and @style="max-width:300px"]//a/@href'
XPATH_PRODUCTS_LIST_YERBA = '//div[@id="gallery-layout-container"]//a/@href'
XPATH_PRODUCTS_LIST_AZUCAR = '//div[@id="gallery-layout-container"]//a/@href'

def parseTipoProducto(url):
    try:
        response = requests.get(url)
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
            #totalProductos = parsed.xpath(XPATH_HOW_MANY_PRODUCTS)[0]
            #print (f'Total de productos: {totalProductos}')
            #print ('\n')
            listadoProductos= parsed.xpath(XPATH_PRODUCTS_LIST_YERBA)
            #print('Estoy en la sub...')
            #print(listadoProductos)
            #print (f'La lista de productos tiene {len(listadoProductos)} elementos.')
            return listadoProductos
        else:
            raise ValueError(f'Error: {response.status_code}')
            return "Error"
        
    except Exception as e:
        print(f'Hubo un error al parsear la pág. de productos de un solo tipo:{e}')
        return "Error"
        