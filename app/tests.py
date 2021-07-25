from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create(username="test", password="pass")


    def test(self):
        self.assertEqual(1, get_user_model().objects.count())

