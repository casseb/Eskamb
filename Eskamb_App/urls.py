from django.conf.urls import url
from Eskamb_App import views


urlpatterns = [
    url(r'^$', views.home),
]