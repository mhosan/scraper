import requests
import lxml.html as html
import sys
import os #para crear carpetas
import datetime  #manejo de fechas

original_stdout = sys.stdout

HOME_URL = 'https://www.larepublica.co/'
XPATH_LINK_TO_ARTICLE = '//text-fill[not(@class)]/a/@href'
XPATH_TITLE = '//div[@class="mb-auto"]/text-fill/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p/text()'

def parse_notice(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            notice = notice.replace('\"', '')
            #with open ('noticias.txt', 'w') as file:
            #    sys.stdout = file
            #    print(notice)
            #    sys.stdout = original_stdout
            parsed = html.fromstring(notice)
            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                title = title.replace('\"', '')
                summary = parsed.xpath(XPATH_SUMMARY)[0]
                body = parsed.xpath(XPATH_BODY)
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
        print(ve)


#def parse_home():
try:
    response = requests.get(HOME_URL)
    if response.status_code == 200:
        home = response.content.decode('utf-8')
        #with open ('prueba.txt', 'w') as f:
        #    sys.stdout = f
        #    print(home)
        #    sys.stdout = original_stdout
        parsed = html.fromstring(home)
        links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
        #print (links_to_notices)
        #print (f'La lista tiene {len(links_to_notices)} elementos. Elemento 0: {links_to_notices[0]}')
        
        today = datetime.date.today().strftime('%d-%m-%Y')
        if not os.path.isdir(today):
            os.mkdir(today)
        for link in links_to_notices:
            parse_notice(link, today)
    else:
        raise ValueError(f'Error: {response.status_code}')
except ValueError as ve:
    print(ve)

