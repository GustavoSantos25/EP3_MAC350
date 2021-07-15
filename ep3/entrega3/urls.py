from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('queryAmostra', views.query1, name='queryAmostra'),
    path('queryExame', views.query2, name='queryExame'),
    path('queryPaciente', views.query2, name='queryPaciente'),
    path('queryProcessamentoAmostra', views.query2, name='queryProcessamentoAmostra')
]
