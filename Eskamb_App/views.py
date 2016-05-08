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

def cadastroPessoaFisica(request):
    template = loader.get_template('cadastro_pessoa_fisica.html')
    return HttpResponse(template.render())

def cadastroPessoaJuridica(request):
    template = loader.get_template('cadastro_pessoa_juridica.html')
    return HttpResponse(template.render())

def meuPerfil(request):
    template = loader.get_template('meu_perfil.html')
    return HttpResponse(template.render())

def editarPerfil(request):
    template = loader.get_template('editar_perfil.html')
    return HttpResponse(template.render())

def queroFaco(request):
    template = loader.get_template('quero_faco.html')
    return HttpResponse(template.render())
