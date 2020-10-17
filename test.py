import requests 
import random

BASE = "http://127.0.0.1:5000/"

# This is already set up in the database this is for visualization purpose.
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
###For input of new message in database###
"""
for i in range(len(data)):

	response = requests.put(BASE+"excuse/"+str(i),data[i])
	print(response.json())
input()
"""
###For updating any message###
"""
x=4#id for which excuse is to be updated
response = requests.patch(BASE+"excuse/"+str(x),{"message":"I can't find reasons to avoid a meeting."})
print(response.json())
input()
"""

n = random.randint(0,len(data)-1)
response = requests.get(BASE+"excuse/"+str(n))
print(response.json())