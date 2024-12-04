from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def aboutPage(request):
    return render(request, 'about/about.html')
def client(request):
    return render(request, 'home/client.html')
def contact(request):
    return render(request, 'home/contact.html')
