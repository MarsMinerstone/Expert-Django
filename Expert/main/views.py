from django.shortcuts import render
from main.models import *

def index(request):
	data = {'disciplines': Discipline.objects.all(), 
			'services': Service.objects.all(), 
			'educations': Education.objects.all(),
			'additions': Addition.objects.all(), 
			'partners': Partner.objects.all()}

	return render(request, 'index.html', data)
