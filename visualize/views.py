from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse

import requests


class indexPageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'visualize/index.html', context={'name':'Sean'})

@csrf_exempt
def send_data(request):
	if request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		body_data = json.loads(body_unicode)
		return HttpResponse(body_data)
		