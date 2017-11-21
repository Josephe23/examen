from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.materia_listar, name ='materia_listar'),
    url(r'^grado/nueva/$', views.grado_nueva, name='grado_nueva'),
    url(r'^materia/nuevo/$', views.materia_nuevo, name= 'materia_nuevo'),
    ]
