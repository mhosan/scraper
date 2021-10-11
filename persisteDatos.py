from pymongo import MongoClient

#conexión:
#con = MongoClient('localhost',27017)  #conexión local
con = MongoClient("mongodb+srv://admin:Ostruca1203@cluster0.rsnsq.mongodb.net/datosprueba?retryWrites=true&w=majority")
db = con.datosprueba
tuiteos = db.tuiteos3
super = db.supermercados
"""
#querys:
#resultado = tuiteos.find({"apporigen":"Twitter for Android"}).limit(1500)
#d = datetime.datetime(2018, 5, 22,8)
#resultado = tuiteos.find({'fecha': {'$gt': d}, 'usuariocompleto':'capitan escabio'}).count()
#resultado = tuiteos.find({'usuariocompleto': None}).count()
#resultado = tuiteos.find({}, {'usuariocompleto':1}).sort('usuariocompleto').limit(10)
#print ('fecha:', resultado['fecha'],'\n','usuario: ', resultado['usuario'])
#print (resultado[0]['fecha'], resultado[99]['fecha'])
#print (resultado)  #el pymongo muestra el cursor (cuando hay mas de un resultado) pero no el contenido...
#print (f"Fecha: {resultado['fecha']}, Usuario: {resultado['usuario']}")
"""
#resultado = tuiteos.find({},{'fecha' : 1, '_id': 0, 'texto': 1}).limit(5000).sort('fecha', pymongo.ASCENDING)
resultado = super.find()
#recorrer un cursor
for elemento in resultado:
    print(elemento)

