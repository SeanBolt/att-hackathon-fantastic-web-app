from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Score
from django.http import HttpResponse
from random import randint


import requests


class indexPageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'visualize/index.html', context={'name':'Sean'})

@csrf_exempt
def send_data(request):
	if request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		parsed_json = json.loads(body_unicode)
		score = Score()
		score.score = parsed_json.get("score")
		score.location = parsed_json.get("location")
		score.save()
		string = "The score posted is" + " " + parsed_json.get("score")
		return HttpResponse(string)


@csrf_exempt
def fetch_data(request):
	if request.method == 'GET':
		score_west = Score.objects.filter(location=1).latest('pk')
		score_east = Score.objects.filter(location=2).latest('pk')
		json1 = {"west":{"pk":score_west.pk, "score": score_west.score, "location": score_west.location},"east":{"pk":score_east.pk, "score": score_east.score, "location": score_east.location}}
		print("hello")
		return HttpResponse(json.dumps(json1))



class scoresPageView(TemplateView):
	def get(self, request, **kwargs):
		scores = Score.objects.all()
		return render(request, 'visualize/score.html', context={"scores":scores})