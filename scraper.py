import sys
import scraperDisco
import scraperVea

original_stdout = sys.stdout

try:
    scraperDisco.procesarLista()
    scraperVea.procesarLista()
except ValueError as ve:
    print(ve)

