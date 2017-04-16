Written by Preet Patel (ppreet) for SI 106 Final Project, Winter 2017
UMID: 56314371

---INSTRUCTIONS---

The chatbot can be run using the command: "python chatbot.py". Note that this works only with Python2.

Besides the interactions pre-loaded in the AIML templates, the chatbot can answer four other queries for the purpose of this project. These are:
1) "What's the weather like in SOMECITY?"
2) "Is it going to rain in SOMECITY this week?"
3) "Is it going to rain in SOMECITY today?"
4) "How cold will it get in SOMECITY this week?"
5) "How cold will it get in SOMECITY today?"
6) "How hot will it get in SOMECITY this week?"
7) "How hot will it get in SOMECITY today?"

Moreover, the chatbot supports caching. This means that once a request has been made, it will be stored locally (even across sessions). This will make response time for duplicate queries fast.

The chatbot can be exited by entering the input "exit".


---SAMPLE INTERACTIONS (ON 31, MARCH 2017)---
(These may vary, since live data is involved)

Query:    "What's the weather like in Paris?"
Response: "In Paris, it is 46.29 and Windy and Partly Cloudy"

Query:    "How cold will it get in Mumbai this week?"
Response: "In Mumbai, it will reach 74.98"

Query:    "Is it going to rain in Tokyo this week?"
Response: "It probably will rain in Tokyo"

Query:    "exit"
Response: ChatBot exits


---OTHER INFORMATION FOR GRADERS---

A. API Failure information: 
    Error messages will be displayed in cases:
        1) Error Message: "Is SOMECITY a city?"
            - If the request to the Google Geocoding API fails
            - If the Google Geocoding API returns a response, but it is either incomplete or lacking (mostly because the input city was invalid)

        2) Error Message: "Sorry, I don't know"        
            - If the request to the DarkSky API fails
            - If the DarkSky API returns a response, but it is either incomplete or lacking
    Note that queries need to be drastically incorrect to throw an error. For example, searching for weather in "somecity" will return a valid result since the APIs correct some queries on their side. Searching for weather in "asdfgh", on the other hand, will throw an error.
    No other error is accounted for.

B. Computing Rain Probability:
    The spec does not tell us where the equality lies in the "Computing Rain Probability" section intervals. I have arbitrarily assigned equality on the lower side. In other words, the intervals are: [0.0, 0.1), [0.1, 0.5), [0.5, 0.9), [0.9, inf).  

C. Caching:
    Both the Google Geocoding and the DarkSky APIs have been cached. This means that once a particular request has been made, the result will be cached. Although this makes the program faster, it has the side effect that the weather will not be updated if you make a duplicate query. Note that this caching will persist even across sessions.
    To clear the cache, either run the command "rm cache.json" in the terminal or delete the file "cache.json" from the directory. Also note that queries that throw an error will not be cached. 
