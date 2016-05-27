from django import forms

from .models import PessoaFisica,Usuario,Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ('tipoContato','conteudo')

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('email','senha','endRua','endNumero','endBairro','endCidade','endEstado','endCep')

class PessoaFisicaForm(forms.ModelForm):

    class Meta:
        model = PessoaFisica
        fields = ('nomeCompleto','formacao')
        
