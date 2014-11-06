from django.test import TestCase, Client, RequestFactory
from views import *

class IndexPageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_userpage_available(self):
        c=Client()
        response = c.get("/users/")
        self.assertEqual(response.status_code, 200)

    def test_addpage_available(self):
        request = self.factory.get('')
        response = add(request)
        self.assertEqual(response.status_code, 200)    