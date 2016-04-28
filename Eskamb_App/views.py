from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())



