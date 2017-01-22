from django.shortcuts import render

def index(request):
    return render(request, 'personal/signin.html')

def home(request):
	return render(request, 'personal/header.html')

def contact(request):
    return render(request, 'personal/basic.html', 
{'content':['If you would like to contact me, email', 'satulya@umich.edu']})

def signin(request):
    return render(request, 'personal/signin.html')

def search_list(request):
    return render(request, 'personal/search_list.html', {'content':['Atulya', 'PBS', 'DOGA']})

def results(request):
    return render(request, 'personal/results.html')

def review(request):
	return render(request, 'personal/review_list.html')

def questionaire(request):
	return render(request, 'personal/questionaire.html')

def edit_profile(request):
	return render(request, 'personal/edit_profile.html')

def view_profile(request):
	return render(request, 'personal/view_profile.html')

# Create your views here.
