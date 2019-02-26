from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	#print(args, kwargs)
	#print(request.user)
	#return HttpResponse("<h1>Welcome to Home</h1><br>")
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	#print(request)
	#return HttpResponse("<h2>Contact Page</h2>")
	return render(request, "contact.html", {})

def about_view(request ,*args, **kwargs):
	#return HttpResponse("<h2>About Page</h2>")
	return render(request, "about.html", {})

def social_view(request,*args, **kwargs):
	#return HttpResponse("<h2>Social Page</h2>")	
	return render(request, "socialpage.html", {})
