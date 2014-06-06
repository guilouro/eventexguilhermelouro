# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r

class DetailTest(TestCase):
	def setUp(self):
		s = Subscription.objects.create(name='Guilherme Louro', cpf='12345678901', email='guilherme-louro@hotmail.com', phone='21-99999-9999')
		self.resp = self.client.get(r('subscriptions:detail', args=[s.pk]))

	def test_get(self):
		'GET /inscricao/1/ should return status 200.'
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

	def test_content(self):
		'Contenxt must gave a subscription instance.'
		subscription = self.resp.context['subscription']
		self.assertIsInstance(subscription, Subscription)

	def test_htmlt(self):
		'Check if subscription data was rendered.'
		self.assertContains(self.resp, 'Guilherme Louro')

class DetailNotFound(TestCase):
	def test_not_found(self):
		response = self.client.get(r('subscriptions:detail', args=[0]))
		self.assertEqual(404, response.status_code)