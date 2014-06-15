# coding: utf-8
from django.conf.urls import patterns, url
from eventex.subscriptions.views import SubscriptionDetail, SubscriptionCreate

urlpatterns = patterns('eventex.subscriptions.views', 
	url(r'^$', SubscriptionCreate.as_view(), name='subscribe'),
	url(r'^(?P<pk>\d+)/$', SubscriptionDetail.as_view(), name='detail'),
)