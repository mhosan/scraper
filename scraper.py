import sys
import scraperDisco

original_stdout = sys.stdout

try:
    scraperDisco.procesarLista()

except ValueError as ve:
    print(ve)

