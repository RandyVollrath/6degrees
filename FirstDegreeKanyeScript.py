" This file is supposed to take the json data from the Rap Genius API"
"that has already been put in a txt file and return it as a list of"
"the song ids"

'''
UPDATED: NOTE TO SELF: MAY NEED TO CHANGE 'kanyeFirstDegreeDict' back to a list because
I want to keep the order (popularity) in tact and I may want to create a dict for the songs API call
'''

import json
#!/usr/bin/python

from pprint import pprint
import requests
from collections import OrderedDict
import sys
import io
import time
from py2neo import Node, Relationship, Graph, authenticate



NEO4J_URL = 'localhost:7474'
NEO4J_USER = 'neo4j'
NEO4J_PASSWORD = 'Swerve1728'
NEO4J_GRAPH = "/db/data/"

authenticate(NEO4J_URL, NEO4J_USER, NEO4J_PASSWORD)
graph = Graph('http://' + NEO4J_URL + NEO4J_GRAPH)
#graph.delete_all()

'''
kanyeCall = requests.get("http://api.genius.com/artists/72/songs?per_page=50&sort=popularity&secondary_artist&featured_artist",
    params={"access_token": "QoaHkyBYNqEmLJk6P3SFdBbm4R_6pXXssK24Wa0WR29MoBFHdG3gUI2IFJFxFFfw"})
'''

with io.open("/Users/randy/PycharmProjects/6degrees/KanyeAllSongs.txt", encoding='utf-8') as data_file:
    data=json.load(data_file)
#    pprint(data)
#Can now process data as python code

kanye = Node("Artist", name="Kanye West")
#print(kanye)
graph.create(kanye)

kanyeFirstDegreeDict = OrderedDict()
#creates an *ordered* dict (ordered by popularity of song)

responseHandling = data["response"]["songs"]
#partially parses JSON

for i,entry in enumerate(responseHandling):
    kanyeFirstDegreeDict[responseHandling[i]["id"]]=responseHandling[i]["title"]
    # adds values to OrderedDict
    # formatd as follows:
    # OrderedDict([(2399676, 'FACTS'), (2403628, 'Real Friends')...
    # with songID has the key and song title as the value


#print (kanyeFirstDegreeDict)
# Prints a dict with the song ids as the key and song title as the value
#print (kanyeFirstDegreeDict)

#EVERYTHING ABOVE THIS LINE HAS BEEN ABOUT PARSING KANYE DATA INTO ORDERED DICT#

primaryArtists=OrderedDict()
kanyeFeaturedArtistsList = []
kanyeFeaturedArtistsDict = {}
apiLimiterCounter=0

for key in kanyeFirstDegreeDict:

    print(key)

##########################Everything here needs to be looped through 1027 times lol
    #time.sleep(1) #delays 1 second!
    resp = requests.get("http://api.genius.com/songs/"+str(key),
            params={"access_token": "QoaHkyBYNqEmLJk6P3SFdBbm4R_6pXXssK24Wa0WR29MoBFHdG3gUI2IFJFxFFfw"})
    #print(resp)
    pythonicData = json.loads(resp.text)
    songsRespHandling = pythonicData["response"]["song"]["featured_artists"]
    #pprint(songsRespHandling)

    nameOfSong = pythonicData["response"]["song"]["title"]

    primaryArtists[pythonicData["response"]["song"]["primary_artist"]["name"]] = pythonicData["response"]["song"]["primary_artist"]["id"]
    #Makes OrderedDict of Primary artist & Artist id

    for i in range(0,len(songsRespHandling)):
        skip = False
        print(i)
        kanyeFeaturedArtistsDict[songsRespHandling[i]["name"]]=songsRespHandling[i]["id"]
        print(kanyeFeaturedArtistsDict)
    #     if songsRespHandling[i]["id"] == 72:
    #         skip = True
    #
    #         kanyeFeaturedArtistsDict.update({nameOfSong:[pythonicData["response"]["song"]["primary_artist"]["name"], pythonicData["response"]["song"]["primary_artist"]["id"]]})
    #         kanyeFeaturedArtistsList.append(kanyeFeaturedArtistsDict.copy())
    #
    #
    #         bob = Node("Artist", name=str(artistName), id=artistId)
    #         graph.create(bob)
    #         kanye_knows_bob = Relationship(kanye, "KNOWS", bob, song=str(nameOfSong))
    #         graph.create(kanye_knows_bob)
    #         #use merge_one
    #
    #     else:
    #         kanyeFeaturedArtistsDict.update({nameOfSong:[songsRespHandling[i]["name"], songsRespHandling[i]["id"]]})
    #         kanyeFeaturedArtistsList.append(kanyeFeaturedArtistsDict.copy())
    #         #print(kanyeFeaturedArtistsList)
    #         bob = Node("Artist", name=str(artistName), song=str(nameOfSong))
    #         #print(str(bob))
    #         kanye_knows_bob = Relationship(kanye, "Collaborated with", bob, song=str(nameOfSong))
    #         #print(str(kanye_knows_bob))
    #         graph.create(kanye_knows_bob)

#non_bmp_map = pythonicData.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
#print(non_bmp_map)

    apiLimiterCounter+=1
    if apiLimiterCounter == 6:
        break

#results=graph.cypher.execute("match (n) where n.name= '{}' return n".format("Kendrick Lamar"))
#where Kendrick Lamar is currently is where I can put a variable and have the song name returned


#print(results.records[0].n.get_properties()["song"])
# python file prints 'No More Parties in LA"


##########################
'''skip = False
        if songsRespHandling[i]["id"] == 72:
            skip = True
            kanyeFeaturedArtistsDict.update({nameOfSong:[pythonicData["response"]["song"]["primary_artist"][i]["name"], pythonicData["response"]["song"]["primary_artist"][i]["id"]]})
            continue
        if songsRespHandling["featured_artists"][i]["id"] != 72:'''
'''
I put the requests code in a loop iterating through 'justFirstDegreeSongIds'.
On each iteration of the loop, I create a unique dict, take the songID,
make an API call using the songID, parse through the results of the API call
to get the featured_artists, use the songTitle as the key to the dict and make
the value a list with the featArtist name as the 0 value and their id 1 value
'''

#updated to include if kanye is the featured artist himself

'''
Now what's next:


'''
