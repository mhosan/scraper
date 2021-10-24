from datetime import datetime
from pymongo import MongoClient


#conexión:
#con = MongoClient('localhost',27017)  #conexión local
con = MongoClient("mongodb+srv://admin:Ostruca1203@cluster0.rsnsq.mongodb.net/datosprueba?retryWrites=true&w=majority")
db = con.datosprueba
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
#resultado = super.find()
#resultado = super.find({'precio' : {'$gt' : 200}, '_id':0})
filtro = {'precio' : {'$gt' : 200}}
projeccion = {'_id': 0}
sort = [('precio', -1)]
#resultado = super.find(filter=filtro, projection=projeccion, sort = sort, limit=2)
#resultado = super.find(filter=filtro, projection=projeccion, sort = sort).limit(2)
#resultado = super.find(filter=filtro, projection=projeccion).limit(5).sort('precio', pymongo.ASCENDING)
#resultado = super.find(filter=filtro, projection=projeccion).limit(5).sort('precio', pymongo.ASCENDING)
#resultado = super.aggregate([{'$group': {'_id': 'super', 'cant':{'$sum':1}} }])
#resultado = super.aggregate([{'$match': {'supermercado': 'Vea'}}, {'$group' : {'_id':'Vea', 'Total Productos': {'$sum': 1}}}])
#resultado = super.aggregate([{'$match': {'supermercado': 'Dia'}}, {'$group' : {'_id':'Dia', 'Total Productos': {'$sum': 1}}}])
resultado = super.aggregate([{'$match': {'supermercado': 'Disco'}}, {'$group' : {'_id':'Disco', 'Total Productos': {'$sum': 1}}}])
for elemento in resultado:
    print(elemento)
