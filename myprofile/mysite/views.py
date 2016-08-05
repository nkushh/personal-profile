from django.shortcuts import render

from .models import About

# Create your views here.
def home(request):
	return render(request, 'mysite/index.html')

def dashboard(request):
	return render(request, 'mysite/dashboard.html')

def about(request):
	me = About.objects.all()
	return render(request, 'mysite/about.html', {'me':me})
