try:
    from main import app
    import unittest
except Exception as e:
    print("Some Modules are Missing {}".format(e))


class FlaskTest(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    def test_index_page_loads(self):
        tester = app.test_client(self)
        response = tester.get("/", content_type="html/text")
        self.assertTrue(b"Hey, We've got You Covered" in response.data)

    def test_index_page1_loads(self):
        tester = app.test_client(self)
        response = tester.get(
            "/question?question=Avoiding an outing plan.", content_type="html/text")
        self.assertTrue(b"Your car has a flat tire." or
                        "You do not have a car, and you do not want anyone going out of their way to give you a ride." or
                        "You rented a movie and have to watch it tonight so you will not be charged for an extra day. That two or three dollars per day really can add up." or
                        "Fake an illness." or
                        "Stress out about how much work you have to do in the next day " or
                        "Family unexpectedly came in from out of town. " in response.data)

    def test_index_page2_loads(self):
        tester = app.test_client(self)
        response = tester.get(
            "/question?question=Chilling on a Wednesday.", content_type="html/text")
        self.assertTrue(b"I am not feeling so well " or
                        "I am vomiting copiously" or
                        "My wallet/phone/identity was stolen!" or
                        "Ugh, my car is in the shop and/or the G train is not running!" or
                        "There is a family/roommate/pet emergency" or
                        "My dog is throwing up" in response.data)

    def test_index_page3_loads(self):
        tester = app.test_client(self)
        response = tester.get(
            "/question?question=Skiping a family function.", content_type="html/text")
        self.assertTrue(b"Have to pick up/drop someone to the airport/railway station. " or
                        "Need to get some paperwork done at a government office." or
                        "Have got work at the bank." or
                        "Cops are coming over for passport verification." or
                        "Need to get the car fixed." or
                        "I have got a stomach infection." in response.data)

    def test_index_page4_loads(self):
        tester = app.test_client(self)
        response = tester.get(
            "/question?question=Buying a dog.", content_type="html/text")
        self.assertTrue(b"Dogs Give Us A Sense Of Purpose " or
                        "Dogs Give Us Confidence" or
                        "Puppies keep you active" or
                        "Puppies help you make friends" or
                        "Puppies are unbelievably cute" or
                        "Puppies lower stress" in response.data)

    def test_index_page5_loads(self):
        tester = app.test_client(self)
        response = tester.get(
            "/question?question=Going for a party.", content_type="html/text")
        self.assertTrue(b" A party celebrates and formalizes the act of officially handing the house over to the homeowners. " or
                        "Friends are good for your immune system" or
                        "Socializing is good for your memory" or
                        "Hosting teaches you to embrace stress" or
                        "You will sleep better" or
                        "Your organizational skills will improve" in response.data)

    def test_index_page6_loads(self):
        tester = app.test_client(self)
        response = tester.get(
            "/question?question=Buying a new car.", content_type="html/text")
        self.assertTrue(b"Buying A  Car Saves Money " or
                        "You Can Upgrade In Life" or
                        "Peace Of Mind" or
                        "Get exactly the spec you want" or
                        "Keep up with the Joneses xD" in response.data)

    def test_index_page7_loads(self):
        tester = app.test_client(self)
        response = tester.get(
            "/question?question=Going for a vacation.", content_type="html/text")
        self.assertTrue(b"My dogs been whining a lot lately. I think he's depressed and its time I take him on a road trip. " or
                        "I want to prepare myself for the zombie apocalypse. I think trekking would help." or
                        "I think we should have our next company retreat in Goa. It will be a great team building exercise." or
                        "Hi boss, I woke up pretty disoriented because I worked really late. I have found myself on a plane to Costa Rica" or
                        "The coffee in the break room is really bad. I volunteer to go to Brazil and pick some up for us." or
                        "My route to work had a lot of traffic so I decided to take another one. Then my GPS stopped working. Somehow, I've reached Goa so I guess I'll be late." in response.data)

    def test_index_page8_loads(self):
        tester = app.test_client(self)
        response = tester.get(
            "/question?question=Bunking classes.", content_type="html/text")
        self.assertTrue(b" I am not well " or
                        "I have relatives coming over so I have to leave early." or
                        "Sports or cultural fest preparation" or
                        "Attending tuitions." or
                        "I was in an accident." or
                        "I have to study for exams" in response.data)


if __name__ == "__main__":
    unittest.main()
