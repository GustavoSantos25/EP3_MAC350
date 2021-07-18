from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('queryAmostra', views.queryAmostra, name='queryAmostra'),
    path('queryExame', views.queryExame, name='queryExame'),
    path('queryPaciente', views.queryPaciente, name='queryPaciente'),
    path('queryProcessamentoAmostra', views.queryProcessamentoAmostra, name='queryProcessamentoAmostra')
]
