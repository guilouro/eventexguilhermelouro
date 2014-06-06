# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r

class SubscribeTest(TestCase):
	
	def setUp(self):
		self.resp = self.client.get(r('subscriptions:subscribe'))

	def test_get(self):
		'GET /inscricao/ must return status code 200.'
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

	def test_html(self):
		'Html must contain input controls.'
		self.assertContains(self.resp, '<form')
		self.assertContains(self.resp, '<input', 6)
		self.assertContains(self.resp, 'type="text"', 3)
		self.assertContains(self.resp, 'type="email"')
		self.assertContains(self.resp, 'type="submit"')

	def test_csrf(self):
		self.assertContains(self.resp, 'csrfmiddlewaretoken')

	def test_has_form(self):
		'Context must have the subscription form.'
		form = self.resp.context['form']
		self.assertIsInstance(form, SubscriptionForm)

	
class SubscribePostTest(TestCase):

	def setUp(self):
		data = dict(name='Guilherme Louro', cpf='12345678901', email='guilherme-louro@hotmail.com', phone='21-99999-9999')
		self.resp = self.client.post(r('subscriptions:subscribe'), data)

	def test_post(self):
		self.assertEqual(302, self.resp.status_code)

	def test_save(self):
		'Valid POST must be saved.'
		self.assertTrue(Subscription.objects.exists())


class SubscribleInvalidPostTest(TestCase):
	def setUp(self):
		data = dict(name='Guilherme Louro', cpf='000000000012', email='guilherme-louro@hotmail.com', phone='21-99999-9999')
		self.resp = self.client.post(r('subscriptions:subscribe'), data)

	def test_post(self):
		self.assertEqual(200, self.resp.status_code)

	def test_form_erros(self):
		'Form must contain errors.'
		self.assertTrue(self.resp.context['form'].errors)

	def test_dont_save(self):
		'Do not save data.'
		self.assertFalse(Subscription.objects.exists())
