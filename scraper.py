import requests
import lxml.html as html

HOME_URL = 'https://www.larepublica.co'
XPATH_LINK_TO_ARTICLE = '//h2[@data-h="17"]/a/@href'
XPATH_TITLE = '//h2[@data-h="45"]/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p/text()'

#def parse_home():
try:
    response = requests.get(HOME_URL)
    if response.status_code == 200:
        home = response.content.decode('utf-8')
        parsed = html.fromstring(home)
        links_to_notices = parsed.xpath('//div')
        print (links_to_notices)
    else:
        raise ValueError(f'Error: {response.status_code}')
except ValueError as ve:
    print(ve)

#def run():
#    parse_home()

#if __name__ == __main__:
#    run()

