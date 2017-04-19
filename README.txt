Written by Preet Patel (ppreet) 

---FILES INCLUDED---

1) chatbot.py - The driver for the chatbot program.
2) cache.json - A partially filled cache for the chatbot. As submitted, the cache contains data about Paris and Chicago.
3) README.txt - This file, which contains information about the chatbot.


---INSTRUCTIONS---

The chatbot can be run using the command: "python chatbot.py". Note that this works only with Python2.

Besides the interactions pre-loaded in the AIML templates, the chatbot can answer seven other queries for the purpose of this project. These are:
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
(These may vary, since live data is involved. These responses do not reflect what the submitted cache holds.)

Query:    "What's the weather like in Paris?"
Response: "In Paris, it is 46.29 and Windy and Partly Cloudy"

Query:    "How cold will it get in Mumbai this week?"
Response: "In Mumbai, it will reach 74.98"

Query:    "Is it going to rain in Tokyo this week?"
Response: "It probably will rain in Tokyo"

Query:    "exit"
Response: ChatBot exits
