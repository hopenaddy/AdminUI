from django.test import TestCase, Client, RequestFactory
from views import *
from my_app.models import Users
from model_mommy import mommy

class IndexPageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_userpage_available(self):
        c=Client()
        response = c.get("/users/")
        print response.content
        self.assertEqual(response.status_code, 200)

    def test_addpage_available(self):
        request = self.factory.get("/users/")
        response = add(request)
        self.assertEqual(response.status_code, 200)

    def test_whatever_creation_mommy(self):
        what = mommy.make(Users)
        self.assertTrue(isinstance(what, Users))
        
