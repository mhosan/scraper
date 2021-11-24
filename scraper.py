import sys
#import scraperDisco
#import scraperVea
import scraperDia

original_stdout = sys.stdout

try:
    #scraperDisco.procesarLista()
    #scraperVea.procesarLista()
    scraperDia.procesarLista()
except ValueError as ve:
    print(ve)


