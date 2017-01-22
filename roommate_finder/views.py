from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from roommate_finder.models import Feature
from roommate_finder.models import ProfileForm
import pdb 

def index(request):
    return HttpResponse("Hello, world. You're at the roommate finder page.")

def portfolio(request):
	features = Feature.objects.all()
	return render(request,'roommate_finder/feature_list.html',{'features':features})

def profile(request):
	#pdb.set_trace()
	#global new_profile
	if request.method == 'POST':
		print request.method
        # create a form instance and populate it with data from the request:
		new_profile = ProfileForm(request.POST, request.FILES)
		# check whether it's valid:
		pdb.set_trace()
		if new_profile.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
			return HttpResponseRedirect('/roomie/profile')

    # if a GET (or any other method) we'll create a blank form
	else:
		new_profile = ProfileForm()
	
	return render(request,'roommate_finder/save_profile.html',{'profile':new_profile})