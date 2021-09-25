import requests
import lxml.html as html
import sys
import os #para crear carpetas
import datetime  #manejo de fechas

original_stdout = sys.stdout

HOME_URL = 'https://www.clarin.com/'

#Links de los titulares principales y secundarios (los secundarios con y sin foto)
XPATH_LINK_TO_ARTICLE_MAIN = '//article[@class="content-nota list-format twoxone_no_foto"]/a[@class="link_article"]/@href'
XPATH_LINK_TO_ARTICLE_SECONDARY = '//article[@class="content-nota list-format onexone_no_foto no-p"]/a[@class="link_article"]/@href'
XPATH_LINK_TO_ARTICLE_SECONDARY_FOTO = '//article[@class="content-nota onexone_foto    list-format flex-change"]/a[@class="link_article"]/@href'

#titulos de las notas del los titulares
XPATH_TITLE_MAIN = '//div[@class="title"]/h1[@id="title"]/text()'

#resumen de las notas principales o titulares
XPATH_SUMMARY_MAIN = '//div[@class="bajada"]/h2/text()'

#cuerpo de la noticia principal
XPATH_BODY_MAIN = '//div[@class="body-nota"]/p/text()'


def parse_notice(link, today):
    try:
        #print ('\n\n')
        #print(f'El link del titular de la nota es: {link}')
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            notice = notice.replace('\"', '')
            """
            with open ('noticiasPpales.txt', 'w') as file:
                sys.stdout = file
                print(notice)
                sys.stdout = original_stdout
            """
            parsed = html.fromstring(notice)
            try:
                title = parsed.xpath(XPATH_TITLE_MAIN)[0]
                title = title.replace('\"', '')
                #print ('\n\n')
                #print(f'El titulo es: {title}')
                summary = parsed.xpath(XPATH_SUMMARY_MAIN)[0]
                #print ('\n\n')
                #print(f'El resumen es: {summary}')
                body = parsed.xpath(XPATH_BODY_MAIN)
                #for item in body:
                #    item = item.replace('\'', '')
                print ('\n\n')
                print(f'El cuerpo de la nota es: {body}')
            except IndexError:
                return
            with open(f'{today}/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
                    f.write('\n')
            
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(f'El error: {ve}')


try:
    response = requests.get(HOME_URL)
    if response.status_code == 200:
        home = response.content.decode('utf-8')
        #with open ('prueba.txt', 'w') as f:
        #    sys.stdout = f
        #    print(home)
        #    sys.stdout = original_stdout
        parsed = html.fromstring(home)
        links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE_MAIN)
        print ('\n')
        print (links_to_notices)
        print ('\n')
        print (f'La lista tiene {len(links_to_notices)} elementos.')
        today = datetime.date.today().strftime('%d-%m-%Y')
        if not os.path.isdir(today):
            os.mkdir(today)
        for link in links_to_notices:
            link = 'https://www.clarin.com' + link 
            parse_notice(link, today)
            
    else:
        raise ValueError(f'Error: {response.status_code}')
except ValueError as ve:
    print(ve)

