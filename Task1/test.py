import requests 
import random

BASE = "http://127.0.0.1:5000/"

# This is already set up in the database this is for visualization purpose.
data = [{ "message": "My dog is throwing up" },
		{ "message": "I have some  work" },
		{ "message": "I have a package I have to sign for" },
		{ "message": "OMG I totally forgot we had plans" },
		{ "message": "I had a stomach full meal I can't move " },
		{ "message": "I totally missed this!" },
		{ "message": "I haven't finished planning yet" },
		{ "message": "It's a work in progress" },
		{ "message": "I've got too many urgent things to do " },
		{ "message": "I Dont have permission" },
		{ "message": "I'm not feeling well" },
		{ "message": "I have work tonight" },
		{ "message": "I have work early tomorrow" },
		{ "message": "Oh, was that tonight" },
		{ "message": "There's a pet emergency " },
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