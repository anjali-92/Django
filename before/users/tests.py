from django.test import TestCase
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    def setup(self):
	print "HELLO"
	User.objects.create_user(username="Zen")
	
    def test_user(self):
	check = User.objects.get(name="Zen")
	self.assertEqual(check,check)
