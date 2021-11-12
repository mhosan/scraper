import requests
import lxml.html as html    #para xpath
import sys

original_stdout = sys.stdout

def parseProductos(url, supermercado):
    if supermercado == "Disco":
        XPATH_PRODUCTS_LIST = '//div[@id="gallery-layout-container"]//a/@href'
    if supermercado == "Vea":
        XPATH_PRODUCTS_LIST = '//div[@id="gallery-layout-container"]//a/@href'
    if supermercado == "Dia":
        XPATH_PRODUCTS_LIST = '//div[@class="prateleira vitrine n1colunas"]//a[@class="product-image"]/@href'
    if supermercado == "Jumbo":
        XPATH_PRODUCTS_LIST = '//div[@class="product-item__image-wrapper"]/a/@href'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            home = response.content.decode('utf-8', errors='replace') #ojo que response.content es un objeto de la clase bytes
                                                                      #con el decode se transforma a str  
            """
            with open ('vea.txt', 'w') as f:
            sys.stdout = f
            print(home)
            sys.stdout = original_stdout
            
            with open(f'paginaVeaLeche.txt', 'w', encoding='utf-8') as f:
                f.write(home)
                f.write('\n\n')
            """
            parsed = html.fromstring(home) #transformar el str a elementos de html
            #totalProductos = parsed.xpath(XPATH_HOW_MANY_PRODUCTS)[0]
            #print (f'Total de productos: {totalProductos}')
            #print ('\n')
            
            listadoProductos= parsed.xpath(XPATH_PRODUCTS_LIST)
            print('\n','Productos a parsear (lista) del super: ', supermercado, ' --->','\n')
            if len(listadoProductos) > 0:
                print(listadoProductos)
            else:
                print('Lista vacia')
                
            print (f'La lista de productos de {supermercado} tiene {len(listadoProductos)} elementos.')
            return listadoProductos
            
        else:
            #raise ValueError(f'Error: {response.status_code}')
            return f'Error: {response.status_code}'
        
    except Exception as e:
        print(f'Hubo un error al parsear la pág. de productos de un solo tipo:{e}')
        return "Error"
        