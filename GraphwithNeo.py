from py2neo import Graph, Node, Relationship
graph=Graph()

#remote_graph= Graph("http://www.oracleofkanye.com")
# may need to input user name and password
#^the above would establish a connection to the server

'''
Building Nodes and Relationships are only in client.
Build Graph and it's in the server/makes a database
'''
#use .pull() method to retreive data from server for client?

kanyeGraph = graph.cypher.begin()
statement = "MATCH (a {name:{A}}), (b {name:{B}}) CREATE (a)-[:KNOWS]->(b)"
#replace 'a' info with kanye's info

# Best approach: Programmatically CREATE artist Nodes first (with song name
# as a property), then programmatically MATCH relationships

# make this list: [("Kanye West", "Kendrick Lamar"), ("Kanye West, "Ty Dolla $ign")
# ...]
#^Forms relationship
# kanyePairings = list of tuples

for artist_a, artist_b in kanyePairings:
    kanyeGraph.append(statement, {"A": artist_a, "B": artist_b})
    #may need a uniqueness_constraint here
    
kanyeGraph.commit()



#when accessing the artist and their song, I will want to access the first song
# in the list of songs because that will be the most popular song


Node("Artist", name="")
Relationship( , "Collaborated with", )

