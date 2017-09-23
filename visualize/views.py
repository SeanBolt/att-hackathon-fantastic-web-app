from django.shortcuts import render
from django.views.generic import TemplateView
import requests


class indexPageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'visualize/index.html', context={'name':'Sean'})