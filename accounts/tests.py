from django.test import TestCase
from django.urls import reverse, resolve
from .views import signup
from django.contrib.auth.forms import UserCreationForm

# Create your tests here.
class SignUpTests(TestCase):

	def setUp(self):
		url = reverse('signup')
		self.response = self.client.get(url)

	def test_signup_status_code(self):
		self.assertEquals(self.response.status_code, 200)

	def test_signup_url_resolves_signup_view(self):
		view = resolve('/signup/')
		self.assertEquals(view.func, signup)

	def test_csfr(self):
		self.assertContains(self.response, 'csrfmiddlewaretoken')

	def test_contains_form(self):
		form = self.response.context.get('form')
		self.asserIsInstance(form, UserCreationForm)

class SuccessfulSignUpTests(TestCase):

	def setUp(self):
		url = reverse('signup')
		data = {
			'username': 'john'
			'password1': 'abcdef123456',
			'password1': 'abcdef123456'
		}
		self.response = self.client.post(url, data)
		self.home_url = reverse('home')

	def test_redirection(self):
		# a valid home submission should redirect the user back to the home page
		self.assertRedirects(self,response, self.home_url)

	def test_user_creation(self):
		self.assertTrue(User.object.exists())







