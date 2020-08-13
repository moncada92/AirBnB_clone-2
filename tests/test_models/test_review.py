#!/usr/bin/python3
""" Unittest for review model """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Test review class """

    def __init__(self, *args, **kwargs):
        """ initialize """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review
        self.value.place_id = "63558d94-08d4-48df-85b4-7b71c90ad951 "
        self.value.user_id = "d4e903c1-3c04-4f32-a2d5-b3802356db50"
        self.value.text = "Nice place"

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)
