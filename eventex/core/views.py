# coding: utf-8
from django.shortcuts import render
from eventex.core.models import Speaker, Talk
from django.views.generic import TemplateView, DetailView

class HomeView(TemplateView):
	template_name = 'index.html'

# def home(request):
# 	return render(request, 'index.html')

class SpeakerDetail(DetailView):
	model = Speaker
# def speaker_detail(request, slug):
# 	speaker = get_object_or_404(Speaker, slug=slug)
# 	context = { 'speaker': speaker }
# 	return render(request, 'core/speaker_detail.html', context)

def talk_list(request):
	context = {
		'morning_talks' : Talk.objects.at_morning(),
		'afternoon_talks' : Talk.objects.at_afternoon(),
	}
	return render(request, 'core/talk_list.html', context)


class TalkDetail(DetailView):
	model = Talk