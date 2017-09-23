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
		items_averaged = 10
		score_west = Score.objects.filter(location=1).order_by('-pk')[:items_averaged]
		score_east = Score.objects.filter(location=2).order_by('-pk')[:items_averaged]

		west_array = []
		east_array = []

		for number in range(0,items_averaged): 
		   	west_array.append(score_west[number].score)
		   	east_array.append(score_east[number].score)

		score_w = sum(west_array)/len(west_array)
		score_e = sum(east_array)/len(east_array)

		json1 = {"west":{"score": score_w},"east":{"score": score_e}}
		print(west_array)
		print(score_w)

		return HttpResponse(json.dumps(json1))



class scoresPageView(TemplateView):
	def get(self, request, **kwargs):
		scores = Score.objects.all()
		return render(request, 'visualize/score.html', context={"scores":scores})