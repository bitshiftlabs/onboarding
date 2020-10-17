import requests 
import random

BASE = "http://127.0.0.1:5000/"


data = [{ "message": "I can't find reasons to avoid an outing plan." },
		{ "message": "I can't find reasons to chill on a Wednesday." },
		{ "message": "I can't find reasons to skip a family function." },
		{ "message": "I can't find reasons to buy a dog." },
		{ "message": "I can't find reasons to avoid a meeting." },
		{ "message": "I can't find reasons to chill at home. " },
		{ "message": "I can't find reasons to wake up late." },
		{ "message": "I can't find reasons to play video games " },
		{ "message": "I can't find reasons to take bath daily " },
		{ "message": "I can't find reasons to tidy my room " },
		{ "message": "I can't find reasons to skip exercise" },
		{ "message": "I can't find reasons to skip my homework" },
		{ "message": "I can't find reasons to not to avoid junk foods", },
		]

"""
BULK ADDITION OF DATA INTO THE DATASET
for i in range(len(data)):

	response = requests.put(BASE+"excuse/"+str(i),data[i])
	print(response.json())
input()
"""
n = random.randint(0,len(data)-1)
response = requests.get(BASE+"excuse/"+str(n))
print(response.json())