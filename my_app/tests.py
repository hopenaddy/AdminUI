from django.test import TestCase, RequestFactory
from views import *
from my_app.models import Users
from model_mommy import mommy

class IndexPageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_userpage_available(self):
        request = self.factory.get("")
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_addpage_available(self):
        request = self.factory.get("")
        response = add(request)
        self.assertEqual(response.status_code, 200)

    def test_editpage_available(self):
        request = self.factory.get("")
        response = edit(request,1)
        print response.content
        self.assertEqual(response.status_code, 200)   
         

    def test_whatever_creation_mommy(self):
        what = mommy.make(Users)
        self.assertTrue(isinstance(what, Users))
    