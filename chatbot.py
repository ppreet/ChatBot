# Written by Preet Patel (ppreet) on March 26, 2017 for SI 106 Final Project

import aiml
import os
import requests
import json

#Application Variables
request_page = "https://maps.googleapis.com/maps/api/geocode/json"
API_KEY = "AIzaSyCR57ivdKJzwKiTQOn0yZEqgy2g6re-q5w"

# kernel is responsible for responding to users
kernel = aiml.Kernel()

#Add files from aiml_data
files = os.listdir("aiml_data")
for file in files:
    kernel.learn(os.path.join('aiml_data', file))

#Helper functions
#Location Request, returns a list: [status, lat, lng]
def google_request(city):

    #Send request to Google for location
    location = requests.get(request_page, params={
        "address": city,
        "key": API_KEY
    })
    loc_json = json.loads(location.text)

    #Check if the Google API fails
    if(loc_json["status"] != "OK"):
        return [0, 0, 0]

    #Isolate lat and lng
    lat = loc_json["results"][0]["geometry"]["location"]["lat"]
    lng = loc_json["results"][0]["geometry"]["location"]["lng"]

    return [1, lat, lng]

#Weather request:
def darksky_request(lat, lng):
    pass

#Teach AI
def response1(first):

    #Make Google request for location
    loc = google_request(first)
    
    #If request failed
    if(loc[0] == 0):
        return "Is {} a city?".format(first)

    return 'Who gives a shit {}'.format(first)
kernel.addPattern("What's the weather like in {first}?", response1)

def response2(first, second):

    #Make Google request for location
    loc = google_request(second)
    
    #If request failed
    if(loc[0] == 0):
        return "Is {} a city?".format(second)

    return "hahahaa {} haha {}".format(first, second)
kernel.addPattern("How {first} will it get in {second} this week?", response2)

def response3(first):
    
    #Make Google request for location
    loc = google_request(first)
    
    #If request failed
    if(loc[0] == 0):
        return "Is {} a city?".format(first)

    return "lololo {}".format(first)
kernel.addPattern("Is it going to rain in {first} this week?", response3)


#Ask for input from user
while(True):

    inp = inp = raw_input("> ")

    #End program
    if(inp == "exit"):
        break

    print "{}".format(kernel.respond(inp))