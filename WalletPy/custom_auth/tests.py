from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User # Required to assign User as a borrower
# Create your tests here.
class CustomAuthTestCase(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.factory = RequestFactory()

    def testRegisterUser(self):

        response = self.client.post('/register/',
                                     {'username': 'quentin', 'email': 'quentin.mimault@orange.fr', 'password1': 'http://127.0.0.1:8000/register/', 'password2' : 'http://127.0.0.1:8000/register/' },
                                     follow = True)
        print("Test register")
        self.assertEqual(response.status_code, 200)

    # def testLogin(self):
    #
    #     login = self.client.login(username='quentin.mimault@orange.fr', password='http://127.0.0.1:8000/register/')
    #     response = self.client.get(reverse('login'))
    #     self.assertEqual(str(response.context['user']), 'testuser1')
    #     print("Test login")
    #     self.assertEqual(response.status_code, 200)
