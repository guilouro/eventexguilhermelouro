# coding: utf-8
from django.test import TestCase 
from eventex.core.models import Speaker, Contact, Talk

class COntactManagerTest(TestCase):
	def setUp(self):
		s = Speaker.objects.create(name='Henrique Bastos', slug='henrique-bastos', url='http://henrique@bastos.net')
		s.contact_set.add(
			Contact(kind='E', value='henrique@bastos.net'),
			Contact(kind='P', value='21-999999999'),
			Contact(kind='F', value='21-22222222'),
		)

	def test_emails(self):
		qs = Contact.emails.all()
		expected = ['<Contact: henrique@bastos.net>']
		self.assertQuerysetEqual(qs, expected)

	def test_phones(self):
		qs = Contact.phones.all()
		expected = ['<Contact: 21-999999999>']
		self.assertQuerysetEqual(qs, expected)

	def test_faxes(self):
		qs = Contact.faxes.all()
		expected = ['<Contact: 21-22222222>']
		self.assertQuerysetEqual(qs, expected)


class PeriodManagerTest(TestCase):
	def setUp(self):
		Talk.objects.create(title='Morning Talk', start_time='10:00')
		Talk.objects.create(title='Afternoon Talk', start_time='12:00')
	
	def test_morning(self):
		'Should return only talks before 12:00.'
		self.assertQuerysetEqual( Talk.objects.at_morning(), ['Morning Talk'], lambda t: t.title )
	
	def test_afternoon(self):
		'Should return only talks after 11:59:59.'
		self.assertQuerysetEqual( Talk.objects.at_afternoon(), ['Afternoon Talk'], lambda t: t.title )
