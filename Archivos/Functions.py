# Algunas referencias: https://neo4j.com/developer/python/
#                      https://neo4j.com/docs/api/python-driver/current/
#                      https://github.com/neo4j/neo4j-python-driver

#Proyecto 2, Algoritmos y estructuras de datos
#Prototipo de las funciones utilizadas para las busquedas
#------------------Integrates------------------
# - Diego Sevilla 17348
# - David Soto 17551
# - Alejandro Tejada 17854

from neo4jrestclient.client import GraphDatabase    
from neo4jrestclient import client
#from neo4j.v1 import GraphDatabase

db = GraphDatabase("http://localhost:7474", username="neo4j", password="1234567")
#uri = "bolt://localhost:7687"
#driver = GraphDatabase.driver(uri, auth=("neo4j", "12345"))

#caracteristica = db.labels.create("Caracteristica")
#genero = db.labels.create("Genero")
#subgenero = db.labels.create("Subgenero")
#videojuego = db.labels.create("Videojuego")

#-------------------Metodos para Llevar en control de Coincidencias--------------
def RecomendacionCaracteristica(caracteristica,listaJ,listaC):
    q = 'MATCH (u:Caracteristica)-[r:VJ]->(m:Videojuego) WHERE u.name="'+caracteristica+'" RETURN u, type(r), m'
    # "db" as defined above
    results = db.query(q, returns=(client.Node, str, client.Node))
    for r in results:
        #print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))
        suma = 0
        index = listaJ.index(r[2]["name"])
        numero = listaC[index]
        suma = numero + 1
        listaC[index] = suma
    return listaC

def RecomendacionInteligencia(inteligencia,listaJ,listaC):
    q = 'MATCH (u:Habilidad)-[r:VJ]->(m:Videojuego) WHERE u.name="'+inteligencia+'" RETURN u, type(r), m'
    # "db" as defined above
    results = db.query(q, returns=(client.Node, str, client.Node))
    for r in results:
        #print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))
        suma = 0
        index = listaJ.index(r[2]["name"])
        numero = listaC[index]
        suma = numero + 1
        listaC[index] = suma
    return listaC    

def RecomendacionEdad(edad,listaJ,listaC):
    q = 'MATCH (u:Edad)-[r:VJ]->(m:Videojuego) WHERE u.name="'+edad+'" RETURN u, type(r), m'
    # "db" as defined above
    results = db.query(q, returns=(client.Node, str, client.Node))
    for r in results:
        #print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))
        suma = 0
        index = listaJ.index(r[2]["name"])
        numero = listaC[index]
        suma = numero + 1
        listaC[index] = suma
    return listaC

def RecomendacionGenero(genero,listaJ,listaC):
    q = 'MATCH (u:Genero)-[r:VJ]->(m:Videojuego) WHERE u.name="'+genero+'" RETURN u, type(r), m'
    # "db" as defined above
    results = db.query(q, returns=(client.Node, str, client.Node))
    for r in results:
        #print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))
        suma = 0
        index = listaJ.index(r[2]["name"])
        numero = listaC[index]
        suma = numero + 1
        listaC[index] = suma
    return listaC

def RecomendacionSubGenero(subgenero,listaJ,listaC):
    q = 'MATCH (u:Subgenero)-[r:VJ]->(m:Videojuego) WHERE u.name="'+subgenero+'" RETURN u, type(r), m'
    # "db" as defined above
    results = db.query(q, returns=(client.Node, str, client.Node))
    for r in results:
        #print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))
        suma = 0
        index = listaJ.index(r[2]["name"])
        numero = listaC[index]
        suma = numero + 1
        listaC[index] = suma
    return listaC

#-------------------Metodo que busca las recomendaciones Finales-----------
def buscarRecomendacionesFinales(maximo,listaC,listaJ):
    listaPosiciones = []
    listaRecomendaciones = []
    listaPosiciones = [i for i,x in enumerate(listaC) if x==maximo]
    for index in listaPosiciones:
        listaRecomendaciones.append(listaJ[index])
    return listaRecomendaciones
