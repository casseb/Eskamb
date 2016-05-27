from django.conf.urls import url
from Eskamb_App import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^home$', views.homeLogin),
    url(r'^cadastro$', views.cadastro),
    url(r'^cadastro_pessoa_fisica$', views.cadastroPessoaFisica, name="cadastro_fisico"),
    url(r'^cadastro_pessoa_juridica$', views.cadastroPessoaJuridica),
    url(r'^meu_perfil$', views.meuPerfil),
    url(r'^editar_perfil$', views.editarPerfil),
    url(r'^quero_faco$', views.queroFaco),
    url(r'^novo_servico$', views.novoServico),
    url(r'^busca$', views.busca),
]