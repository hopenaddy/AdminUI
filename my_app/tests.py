from django.test import TestCase, RequestFactory
from views import *
from my_app.models import Users
from model_mommy import mommy

class IndexPageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user=Users()

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
        self.assertEqual(response.status_code, 200)

    def test_whatever_creation_mommy(self):
        what = mommy.make(Users)
        self.assertTrue(isinstance(what, Users))

    def test_user_save(self):
        request = self.factory.post("/users/", {"login":"test_user",
                                    "fullname":"test_fullname","token":"test_token"})
        response = user_save(request, self.user)
        self.assertEqual(Users.objects.get(login="test_user").login, "test_user")    
        Users.objects.filter(login="test_user").delete()

    def test_user_delete(self):
        self.user.login="test_user"
        self.user.fullname="test_fullname"
        self.user.token="test_token"
        self.user.save()
        id = Users.objects.get(login="test_user").id
        request = self.factory.post("/users/", {"delete":id})
        response = index(request)
        self.assertEqual(not Users.objects.filter(id=id), True)

    def test_send_page(self):
        user=Users()
        request = self.factory.post("/users/")
        response = send_page(request, self.user)
        self.assertEqual(response.content, add(request).content)