from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def balaji(request):
    return HttpResponse('<h1> <i> <marquee> Balaji is a Good Boy </marquee> </i> </h1>')