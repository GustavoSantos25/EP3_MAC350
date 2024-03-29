from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from collections import namedtuple
from django.template import loader

def index(request):
    return HttpResponse("MAC0350: EP3")
    
def queryPaciente(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM entrega3_paciente')
        result = named_tuple_fetchall(cursor)
    
    template = loader.get_template('queryPaciente.html')
    context = {'queryPaciente_result_list': result,}
    
    return HttpResponse(template.render(context, request))

def queryExame(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT e.tipo, e.virus, p.nome nome_paciente FROM entrega3_exame e\
                        INNER JOIN entrega3_paciente p\
                        ON p.id = e.paciente_id')
        result = named_tuple_fetchall(cursor)
    
    template = loader.get_template('queryExame.html')
    context = {'queryExame_result_list': result,}
    
    return HttpResponse(template.render(context, request))

def queryAmostra(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM entrega3_amostra')
        result = named_tuple_fetchall(cursor)
    
    template = loader.get_template('queryAmostra.html')
    context = {'queryAmostra_result_list': result,}
    
    return HttpResponse(template.render(context, request))

def queryProcessamentoAmostra(request):
    with connection.cursor() as cursor:
        cursor.execute('\
                SELECT a.amostra_id, a.data_de_realizacao - a.data_de_solicitacao tempo_processamento\
                FROM entrega3_paciente_exame_amostra a\
                ORDER BY a.data_de_realizacao - a.data_de_solicitacao\
                LIMIT 5')
        result = named_tuple_fetchall(cursor)
    print(result)
    template = loader.get_template('queryProcessamentoAmostra.html')
    context = {'queryProcessamentoAmostra_result_list': result,}
    
    return HttpResponse(template.render(context, request))

#metodos auxiliares
def named_tuple_fetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    result = [nt_result(*row) for row in cursor.fetchall()]

    return result

