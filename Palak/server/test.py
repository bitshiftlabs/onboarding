'''importing required modules'''
import unittest
from api import app

class Testing(unittest.TestCase):
    '''Testing class for uniy testing'''
    def test_home(self):
        '''tests for status code when a get request is made to home page'''
        tester =app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_home_content(self):
        '''tests for the content type of home page returned'''
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    def test_get_a_reason_1(self):
        '''tests whether the returned information belongs to the requested page'''
        tester = app.test_client(self)
        response = tester.get("/reasons/buy a dog", content_type="html/text")
        self.assertTrue(b"Dogs make Us Laugh" or
                    "Dogs are loyal" or
                    "we're more social with a dog" or
                    "Dogs keep Us Healthy" or
                    "We are more active with dogs"or
                    "Dogs save lives"or
                    "Dogs give Us a sense of purpose"or
                    "Dogs give us confidence"or
                    "Dogs make Us Genuinely Happy"or
                    "Dogs are faithful and responsible" in response.data)

    def test_get_a_reason_2(self):
        '''tests whether the returned information belongs to the requested page'''
        tester = app.test_client(self)
        response = tester.get("/reasons/cancel a trip", content_type="html/text")
        self.assertTrue(b"Sorry,I'm not feeling well today"or
                         "I don't have money."or
                         "I don't have my own vehicle"or
                         "I am quarantined"or
                         "I am tired."or
                         'Sorry,I have planned a trip today'or
                         "Sorry, My mom is ill"or
                         "Sorry,I am ill"or
                         "Sorry,my dad is ill"or
                         "I drank too much last night" in response.data)
    def test_get_a_reason_3(self):
        '''tests whether the returned information belongs to the requested page'''
        tester = app.test_client(self)
        response = tester.get("/reasons/chill on a wednesday", content_type="html/text")
        self.assertTrue(b"It's my choice"or
                                "As I have finished my work on tuesday"or
                                "I am quarantined"or
                                "I have scored full marks in my exam"or
                                "My exams are finished"or
                                "I have nothing to do" in response.data)

    def test_wrong_key_error(self):
        '''tests if the 404 error gives correct response to the user'''
        tester = app.test_client(self)
        response = tester.get("/reasons/guhijlkouih", content_type="html/text")
        self.assertTrue(b"Error:404:Key does not exist" in response.data)

if __name__ =='__main__':
    unittest.main()
