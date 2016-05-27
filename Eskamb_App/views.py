from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader
from .forms import PessoaFisicaForm
from Eskamb_App.forms import UsuarioForm, ContatoForm
from django.db.transaction import commit
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
    formUsuario = UsuarioForm()
    formContato = ContatoForm()
    formPessoa = PessoaFisicaForm()
    if formContato.is_valid() and formUsuario.is_valid() and formPessoa:
        postContato = formContato.save()
        postUsuario = formUsuario.save(commit=False)
        postUsuario.contato = postContato
        postUsuario.save()
        postPessoa = formPessoa.save(commit=False)
        postPessoa.usuario = postUsuario
        postPessoa.save()
    return render(request, 'cadastro_pessoa_fisica.html', {'formPessoa': formPessoa,'formUsuario': formUsuario,'formContato': formContato})

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

def novoServico(request):
    template = loader.get_template('novo_servico.html')
    return HttpResponse(template.render())

def busca(request):
    template = loader.get_template('busca.html')
    return HttpResponse(template.render())