import requests
import random
import json

# Retrives a random word form random word generator 
def get_randomWord():
    url = "https://randomwordgenerator.com/json/words_ws.json"
    response = requests.request("GET",url)
    return_results = response.json()
    randomNumber= random.randint(1,3256)
    randomWord = return_results['data'][randomNumber]["word"]["value"]
    return randomWord