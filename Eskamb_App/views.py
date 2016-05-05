from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader
# -*- coding: utf-8 -*-

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def homeLogin(request):
    template = loader.get_template('index_login.html')
    return HttpResponse(template.render())

def cadastro(request):
    template = loader.get_template('cadastro.html')
    return HttpResponse(template.render())
