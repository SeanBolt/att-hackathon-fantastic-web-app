from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Score
from django.http import HttpResponse
from random import randint


import requests

buffer_west = [1,2,3]
buffer_east = [1,2,3]

peak_west = 1
peak_east = 1

class indexPageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'visualize/index.html', context={'name':'Sean'})

@csrf_exempt
def send_data(request):
	if request.method == 'POST':

		body_unicode = request.body.decode('utf-8')
		print(body_unicode)
		parsed_json = json.loads(body_unicode)
		score = Score()
		score.score = parsed_json.get("score")
		score.location = parsed_json.get("location")
		score.save()
		string = "The score posted is" + " " + parsed_json.get("score")
		print(string)
		
		score_w, score_e = average_scores()

		resp = {"current_fresh": str(round(score_w)), "peak_fresh": str(round(peak_west)), "current_senior": str(round(score_e)), "peak_senior": str(round(peak_east)) }

		return HttpResponse(json.dumps(resp))


@csrf_exempt
def fetch_data(request):
	
	if request.method == 'GET':
		score_w, score_e = average_scores()

		buffer_east.pop()
		buffer_west.pop()

		buffer_east.insert(0, score_e)
		buffer_west.insert(0, score_w)

		if buffer_east.count(buffer_east[0]) == len(buffer_east):
			score_e = 0

		if buffer_west.count(buffer_west[0]) == len(buffer_west):
			score_w = 0

		json1 = {"west":{"score": score_w, "peak": peak_west},"east":{"score": score_e, "peak": peak_east}}

		return HttpResponse(json.dumps(json1))

def average_scores():
	items_averaged = 30
	
	score_west = Score.objects.filter(location=1).order_by('-pk')[:items_averaged]
	score_east = Score.objects.filter(location=2).order_by('-pk')[:items_averaged]

	west_array = []
	east_array = []

	for number in range(0,items_averaged): 
	   	west_array.append(score_west[number].score)
	   	east_array.append(score_east[number].score)

	score_w = sum(west_array)/len(west_array)
	score_e = sum(east_array)/len(east_array)

	global peak_west, peak_east

	if score_w > peak_west:
		peak_west = score_w
	if score_e > peak_east:
		peak_east = score_e

	return score_w, score_e




class scoresPageView(TemplateView):
	def get(self, request, **kwargs):
		scores = Score.objects.all()
		return render(request, 'visualize/score.html', context={"scores":scores})