from flask import Flask, request
from py2neo import Node, Relationship, Graph, authenticate, neo4j

app = Flask(__name__, static_url_path='')


NEO4J_URL = 'localhost:7474'
NEO4J_USER = 'neo4j'
NEO4J_PASSWORD = 'Swerve1728'
NEO4J_GRAPH = "/db/data/"

authenticate(NEO4J_URL, NEO4J_USER, NEO4J_PASSWORD)
graph = Graph('http://' + NEO4J_URL + NEO4J_GRAPH)


@app.route("/")
def hello():
    results=graph.cypher.execute("match (n) where n.name= '{}' return n".format(request.args.get('artist', '')))
    return results.records[0].n.get_properties()["song"]

@app.route("/home")
def home():
    return app.send_static_file('index.html')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == "__main__":
    app.debug = True
    app.run()
