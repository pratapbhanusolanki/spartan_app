from django.http import HttpResponse
from django.shortcuts import render
from roommate_finder.models import Feature

def index(request):
    return HttpResponse("Hello, world. You're at the roommate finder page.")

def portfolio(request):
	features = Feature.objects.all()
	return render(request,'roommate_finder/feature_list.html',{'features':features})