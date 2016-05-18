from __future__ import unicode_literals

from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length = 100)
    aprovado = models.CharField(max_length = 1)
    
    def __str__(self):
        return self.nome
    
#######################################################

class Formacao(models.Model):
    descricao = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.descricao
    
#######################################################

class Contato(models.Model):
    tipoContato = models.CharField(max_length = 2)
    conteudo = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.conteudo
    
#######################################################

class Usuario(models.Model):
    email = models.CharField(max_length = 100)
    senha = models.CharField(max_length = 100)
    contato = models.ForeignKey(Contato)
    endRua = models.CharField(max_length = 100)
    endNumero = models.IntegerField()
    endBairro = models.CharField(max_length = 100)
    endCidade = models.CharField(max_length = 100)
    endEstado = models.CharField(max_length = 2)
    endCep = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.email
    