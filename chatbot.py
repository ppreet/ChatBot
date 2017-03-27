# Written by Preet Patel (ppreet) on March 26, 2017 for SI 106 Final Project

import aiml
import os
import requests
import json

#Application Variables
#https://developers.google.com/maps/documentation/geocoding/intro
goog_request_page = "https://maps.googleapis.com/maps/api/geocode/json"
GOOG_API_KEY = "AIzaSyCR57ivdKJzwKiTQOn0yZEqgy2g6re-q5w"
#https://darksky.net/dev/
DS_API_KEY = "4f43e470ffd89f1410ad770ee1385099"
ds_request_page = "https://api.darksky.net/forecast/" + DS_API_KEY + "/"

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
    location = requests.get(goog_request_page, params={
        "address": city,
        "key": GOOG_API_KEY
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

    weather = requests.get(ds_request_page + str(lat) + "," + str(lng))
    weather_json = json.loads(weather.text)

    return weather_json


#Teach AI
def response1(first):

    #Make Google request for location
    loc = google_request(first)
    
    #If request failed
    if(loc[0] == 0):
        return "Is {} a city?".format(first)

    #Make DarkSky request for weather
    weather = darksky_request(loc[1], loc[2])
    
    #Parse response
    try:
        current = weather["currently"]
        return 'In {}, it is '.format(first) + str(current["temperature"]) + " and " + current["summary"]
    except:
        return "Sorry, I don't know"
kernel.addPattern("What's the weather like in {first}?", response1)

def response2(first, second):

    #Make Google request for location
    loc = google_request(second)
    
    #If request failed
    if(loc[0] == 0):
        return "Is {} a city?".format(second)

    #Make DarkSky request for weather
    weather = darksky_request(loc[1], loc[2])

    #Parse response
    try:
        #Dictionary search term
        search = ""
        if(first == "hot"):
            search = "temperatureMax"
        else:
            search = "temperatureMin"

        week_data = weather["daily"]["data"]
        week_temps = [x[search] for x in week_data]
        print week_temps

        extreme = 0.0
        if(first == "hot"):
            extreme = max(week_temps)
        else:
            extreme = min(week_temps)

        return "In {}, ".format(second) + " it will reach " + str(extreme)
    except:
        return "Sorry, I don't know"
kernel.addPattern("How {first} will it get in {second} this week?", response2)

def response3(first):
    
    #Make Google request for location
    loc = google_request(first)
    
    #If request failed
    if(loc[0] == 0):
        return "Is {} a city?".format(first)

    #Make DarkSky request for weather
    weather = darksky_request(loc[1], loc[2])

    #Parse response
    
    return "hi"
kernel.addPattern("Is it going to rain in {first} this week?", response3)


#Ask for input from user
while(True):

    inp = inp = raw_input("> ")

    #End program
    if(inp == "exit"):
        break

    print "{}".format(kernel.respond(inp))


#Powered by Dark Sky: https://darksky.net/poweredby/