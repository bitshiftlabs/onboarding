from flask import Flask, render_template, request 
import random

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")


reasons={
	  "Avoid an outing plan.":[ "Your car has a flat tire.",
								"You do not have a car, and you do not want anyone going out of their way to give you a ride.",
								"You rented a movie and have to watch it tonight so you will not be charged for an extra day. That two or three dollars per day really can add up.",
								"Fake an illness.",
								"Stress out about how much work you have to do in the next day ",
								"Family unexpectedly came in from out of town. "
								],

	  "Chill on a Wednesday.":["I’m not feeling so well ",
	  						   "I’m vomiting copiously",
	  						   "My wallet/phone/identity was stolen!",
	  						   "Ugh, my car is in the shop and/or the G train isn’t running!",
	  						   "There’s a family/roommate/pet emergency",
	  						   "My dog is throwing up"
	  						   ],

	  "Skip a family function.":["Have to pick up/drop someone to the airport/railway station. ",
	  							 "Need to get some paperwork done at a government office.",
	  							 "Have got work at the bank.",
	  							 "Cops are coming over for passport verification.",
	  							 "Need to get the car fixed.",
	  							 "I've got a stomach infection."
	  							 ],

	  "Buy a dog.":["Dogs Give Us A Sense Of Purpose ",
	  				"Dogs Give Us Confidence",
	  				"Puppies keep you active",
	  				"Puppies help you make friends",
	  				"Puppies are unbelievably cute",
	  				"Puppies lower stress"
	  				],

	  "Go for a party.":[" A party celebrates and formalizes the act of officially handing the house over to the homeowners. ",
	  				     "Friends are good for your immune system",
	  				     "Socializing is good for your memory",
	  				     "Hosting teaches you to embrace stress",
	  				     "You’ll sleep better",
	  				     "Your organizational skills will improve"
	  				     ],

	  "Buy a new car.":["Buying A  Car Saves Money ",
	  					"You Can Upgrade In Life",
	  					"Peace Of Mind",
	  					"Get exactly the spec you want",
	  					"Keep up with the Joneses xD",
	  					],

	  "Go for a vacation.":["My dogs been whining a lot lately. I think he's depressed and its time I take him on a road trip. ",
	  						"I want to prepare myself for the zombie apocalypse. I think trekking would help.",
	  						"I think we should have our next company retreat in Goa. It will be a great team building exercise.",
	  						"Hi boss, I woke up pretty disoriented because I worked really late. I have found myself on a plane to Costa Rica",
	  						"The coffee in the break room is really bad. I volunteer to go to Brazil and pick some up for us.",
	  						"My route to work had a lot of traffic so I decided to take another one. Then my GPS stopped working. Somehow, I've reached Goa so I guess I'll be late."
	  						],

	  "Bunk classes.":[" I am not well ",
	  				   "I have relatives coming over so I have to leave early.",
	  				   "Sports or cultural fest preparation",
	  				   "Attending tuitions.",
	  				   "I was in an accident.",
	  				   "I have to study for exams"],
	  }

@app.route('/question')
def question():
	question = request.args.get("question")
	if question in reasons:
		list_reasons=reasons.get(question)
		n = random.randint(0,len(list_reasons)-1)
		message=list_reasons[n]
	return message

if __name__== "__main__":
	app.run(debug=True)