'''
Extracting data from database
'''

from py2neo import Node, Relationship, Graph, authenticate, neo4j

# authenticate("http://localhost:7474/browser/", "neo4j", "mypassword")

# graph=Graph("http://neo4j:mypassword@localhost:7474/browser/")


NEO4J_URL = 'localhost:7474'
NEO4J_USER = 'neo4j'
NEO4J_PASSWORD = 'Swerve1728'
NEO4J_GRAPH = "/db/data/"

authenticate(NEO4J_URL, NEO4J_USER, NEO4J_PASSWORD)
graph = Graph('http://' + NEO4J_URL + NEO4J_GRAPH)



