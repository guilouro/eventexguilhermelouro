# coding: utf-8
from django.test import TestCase
from datetime import datetime
from django.db import IntegrityError
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):

	def setUp(self):
		self.obj = Subscription(
			name = 'Guilherme Louro',
			cpf = '12345678901',
			email='guilherme-louro@hotmail.com',
			phone='24-99999-9999'
		)

	def test_create(self):
		'Subscription must have name, cpf, email, phone'
		self.obj.save()
		self.assertEqual(1, self.obj.pk)

	def test_has_created_at(self):
		'Subscription must have automatic created_at'
		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)

	def test_unicode(self):
		self.assertEqual(u'Guilherme Louro', unicode(self.obj))


class SubscriptionUniqueTest(TestCase):

	def setUp(self):
		Subscription.objects.create(name='Guilherme Louro', cpf='12345678901', 
									email='guilherme-louro@hotmail.com', phone='24-99999-9999')

	def test_cpf_unique(self):
		s = Subscription(name='Guilherme Louro', cpf='12345678901',
						email='guilherme-louro@hotmail.com', phone='24-99999-9999')
		self.assertRaises(IntegrityError, s.save)

	def test_email_unique(self):
		s = Subscription(name='Guilherme Louro', cpf='12345678902',
						email='guilherme-louro@hotmail.com', phone='24-99999-9999')
		self.assertRaises(IntegrityError, s.save)
