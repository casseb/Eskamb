from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader
# -*- coding: utf-8 -*-

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())



