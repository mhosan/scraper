from datetime import datetime
from pymongo import MongoClient
#import datetime

#conexión:
#con = MongoClient('localhost',27017)  #conexión local
con = MongoClient("mongodb+srv://admin:Ostruca1203@cluster0.rsnsq.mongodb.net/datosprueba?retryWrites=true&w=majority")
db = con.datosprueba
super = db.supermercados

resultado = super.find()
   
contador = 0
#elemenToFind1 = "Leche Entera Clasica La Serenisima Sachet"
#elemenToFind2 = "Leche Entera Clasica La Serenísima Sachet"
#elemenToFind1 = "Yerba Mate Playadito Suave X1kg" #vea y disco
#elemenToFind2 = "Yerba Mate Playadito Suave 1 Kg" #dia
#elemenToFind1 = "Galletitas Oreo Original X 354 Gr" #vea y disco
#elemenToFind2 = "Galletitas Oreo 354 Gr." #dia
elemenToFind1 = "Arroz Largo Fino Gallo X 1 Kg" #vea y disco
elemenToFind2 = "Arroz Gallo Largo Fino 1 Kg." #dia
#elemenToFind1 = "Suprema De Pollo" #vea y disco
#elemenToFind2 = "Suprema de Pollo" #dia

for elemento in resultado:
    try:
        if elemenToFind1 in elemento['descrip'] or elemenToFind2 in elemento['descrip']:
            contador = contador + 1
            """
            if contador == 1:
                dia = datetime.strftime(elemento["fecha"], "%d")
                mes = datetime.strftime(elemento["fecha"], "%m")
                anio = datetime.strftime(elemento["fecha"], "%Y")
            diaNextElement = datetime.strftime(elemento["fecha"], "%d")
            mesNextElement = datetime.strftime(elemento["fecha"], "%m")
            """ 
            fecha = datetime.strftime(elemento["fecha"], "%d-%m-%Y")
            super = elemento["supermercado"]
            #if dia == diaNextElement and mes == mesNextElement:
            #    print(f'Super:{super}, ({contador}), {elemento["descrip"]}, precio: {elemento["precio"]}, fecha: {elemento["fecha"]}')
            print(f'Super:{super}, ({contador}), {elemento["descrip"]}, precio: {elemento["precio"]}, fecha: {fecha}')
    except Exception as e:
        print(f'Error: {e}, en el documento (o registro): {elemento}')