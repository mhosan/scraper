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
elemenToFind = "Leche"
for elemento in resultado:
    if elemenToFind in elemento['descrip']:
        contador = contador + 1
        if contador == 1:
            dia = datetime.strftime(elemento["fecha"], "%d")
            mes = datetime.strftime(elemento["fecha"], "%m")
            anio = datetime.strftime(elemento["fecha"], "%Y")
        diaNextElement = datetime.strftime(elemento["fecha"], "%d")
        mesNextElement = datetime.strftime(elemento["fecha"], "%m")
        super = elemento["supermercado"]
        if dia == diaNextElement and mes == mesNextElement:
            print(f'Super:{super}, ({contador}){elemenToFind}: {elemento["descrip"]} , fecha: {elemento["fecha"]}')
