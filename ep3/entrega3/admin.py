from django.contrib import admin
from .models import Exame, Paciente, Amostra, Paciente_Exame_Amostra

# Register your models here.

admin.site.register(Exame)
admin.site.register(Paciente)
admin.site.register(Amostra)
admin.site.register(Paciente_Exame_Amostra)