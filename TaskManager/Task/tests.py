from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, APITestCase
from rest_framework import status
from rest_framework_jwt.compat import get_user_model
User = get_user_model()

'''
Database is dropped after every test case is executed

login_url='/api-token-auth/'
data={'username':'admin','password':'admin'}
response = client.post(login_url,dataw)

url = '/task/todolist/'
data1 = {'duration_needed': '4', 'name': 'OpenMP'}
auth = 'JWT {0}'.format(response.data['token'])
resp = client.post(url,data1,HTTP_AUTHORIZATION=auth,format='json')

middlewares,
decorators,
context processors,
models

'''
class AuthTokenTests(APITestCase):
    def setUp(self):
        print "in setup"
        self.email = 'admin@admin.com'
        self.username = 'admin'
        self.password = 'admin'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.factory = APIRequestFactory()
        self.api_client = APIClient()
        self.login_url='/api-token-auth/'
        self.data={'username':'admin','password':'admin'}

    def test_get_token(self):
        """
            to get auth token of JWT from middleware
        """
        print "in get token"
        response = self.api_client.post(self.login_url,self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pass

    def tearDown(self):
        print "In tear down"
        pass
