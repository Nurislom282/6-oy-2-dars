from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

def home (request: WSGIRequest):
    return render(request,'index.html')

def page2 (request: WSGIRequest):
    return render(request, 'page 2.html')

def page3 (request: WSGIRequest):
    return render(request, 'page 3.html')

def page4 (request: WSGIRequest):
    return render(request, 'page 4.html')

def page5 (request: WSGIRequest):
    return render(request, 'page 5.html')

def page6 (request: WSGIRequest):
    return render(request, 'page 6.html')

def page7 (request: WSGIRequest):
    return render(request, 'page 7.html')

def page8 (request: WSGIRequest):
    return render(request, 'page 8.html')

def page9 (request: WSGIRequest):
    return render(request, 'page 9.html')

def page10 (request: WSGIRequest):
    return render(request, 'page 10.html')
