import requests
import lxml.html as html    #para xpath

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
            print(listadoProductos)
            print (f'La lista de productos tiene {len(listadoProductos)} elementos.')
            return listadoProductos
        else:
            raise ValueError(f'Error: {response.status_code}')
        
    except Exception as e:
        print(f'Hubo un error al parsear la pág. de productos de un solo tipo:{e}')
        return "Error"
        