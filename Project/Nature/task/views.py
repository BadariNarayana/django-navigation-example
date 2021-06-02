from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request,'task/index.html')
def About(request):
	return render(request,'task/About.html')
def Contact(request):
	return render(request,'task/Contact.html')