from django.conf.urls import url
from Eskamb_App import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^home$', views.homeLogin),
    url(r'^cadastro$', views.cadastro),
    url(r'^cadastro_pessoa_fisica$', views.cadastroPessoaFisica),
    url(r'^cadastro_pessoa_juridica$', views.cadastroPessoaJuridica),
    url(r'^meu_perfil$', views.meuPerfil),
]