# coding: utf-8
from django import forms
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from eventex.subscriptions.models import Subscription

def CPFValidator(value):
	if not value.isdigit():
		raise ValidationError(_(u'CPF deve conter apenas números'))
	if len(value) != 11:
		raise ValidationError(_(u'CPF deve conter 11 dígitos'))

class SubscriptionForm(forms.ModelForm):
	class Meta:
		model = Subscription
		fields = ('name', 'email', 'cpf', 'phone',)
		# exclude = ('paid',)

	def __init__(self, *args, **kwargs):
		super(SubscriptionForm, self).__init__(*args, **kwargs)

		self.fields['cpf'].validators.append(CPFValidator)

		# slide 145