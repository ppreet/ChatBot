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
#Cache file
CACHE_FNAME = "cache.json"

# kernel is responsible for responding to users
kernel = aiml.Kernel()

#Add files from aiml_data
files = os.listdir("aiml_data")
for file in files:
    kernel.learn(os.path.join('aiml_data', file))

#Helper functions
#Location Request, returns a list: [status, lat, lng]
def google_request(city):

    try:
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

    except:
        return [0, 0, 0]

    return [1, lat, lng]

#Weather request: returns the entire response json object
def darksky_request(lat, lng):

    #Open cache file
    try:
        cache_file = open(CACHE_FNAME, 'r')
        cache_contents = cache_file.read()
        cache_file.close()
        cache_diction = json.loads(cache_contents)
    except:
        cache_diction = {}

    url = ds_request_page + str(lat) + "," + str(lng)

    #Send request and update cache file if request not in cache
    if url not in cache_diction:

        try:
            weather = requests.get(url)
            weather_json = json.loads(weather.text)

            #Update cache_diction
            cache_diction[url] = weather.text

            # write the updated cache file
            cache_file = open(CACHE_FNAME, 'w')
            cache_file.write(json.dumps(cache_diction))
            cache_file.close()
            
        except:
            return "API REQUEST FAILED"

        return weather_json
    
    #Else, just return cached value
    return json.loads(cache_diction[url])

#Teach AI
def response1(first):

    #Make Google request for location
    loc = google_request(first)
    
    #If request failed
    if(loc[0] == 0):
        return "Is {} a city?".format(first)

    #Make DarkSky request for weather
    weather = darksky_request(loc[1], loc[2])

    #Error check
    if(weather == "API REQUEST FAILED"):
        return "Sorry, I don't know"
    
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

    #Error check
    if(weather == "API REQUEST FAILED"):
        return "Sorry, I don't know"

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
        #print week_temps

        extreme = 0.0
        if(first == "hot"):
            extreme = max(week_temps)
        else:
            extreme = min(week_temps)

        return "In {},".format(second) + " it will reach " + str(extreme)
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
    #print json.dumps(weather["daily"], indent = 4)

    #Error check
    if(weather == "API REQUEST FAILED"):
        return "Sorry, I don't know"

    #Parse response
    try:

        product = 1
        daily = weather["daily"]
        #print json.dumps(daily["data"], indent=4)
        for i in range(7):
            #print daily["data"][i]["precipProbability"]
            product = product*(1 - daily["data"][i]["precipProbability"])
        
        rain_prob = 1 - product

        #Return statements
        if(rain_prob < 0.1):
            return "It will definitely not rain in {}".format(first)
        elif(rain_prob < 0.5):
            return "It probably will not rain in {}".format(first)
        elif(rain_prob < 0.9):
            return "It probably will rain in {}".format(first)
        else:
            return "It will definitely rain in {}".format(first)

    except:
        return "Sorry, I don't know"
kernel.addPattern("Is it going to rain in {first} this week?", response3)


#Ask for input from user
while(True):

    inp = inp = raw_input("> ")

    #End program
    if(inp == "exit"):
        break

    print "{}".format(kernel.respond(inp))


#Powered by Dark Sky: https://darksky.net/poweredby/