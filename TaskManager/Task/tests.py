from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, APITestCase
'''
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
        self.factory = APIRequestFactory()
        self.api_client = APIClient()
        login_url='/api-token-auth/'
        data={'username':'admin','password':'admin'}

    def test_get_token(self):
        """
            to get auth token of JWT from middleware
        """
        print "in get token"
        pass

    def tearDown(self):
        print "In tear down"
        pass
