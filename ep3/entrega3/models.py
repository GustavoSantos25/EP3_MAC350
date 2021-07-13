from django.db import models

class Paciente(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    nascimento = models.DateField('data de nascimento')
    
    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['cpf'], name='unique_cpf')
                ]
    
    def __str__(self):
        return self.cpf +','+ self.nome +','+ self.endereco +','+ self.nascimento 

class Exame(models.Model):
    tipo = models.CharField(max_length=255)
    virus = models.CharField(max_length=255)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    
    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['tipo', 'virus'], name='unique_tipo_virus')
                ]

    def __str__(self):
        return self.tipo +','+ self.virus +','+ self.id_paciente

class Amostra(models.Model):
    codigo_amostra = models.CharField(max_length=255)
    metodo_de_coleta = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    
    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['codigo_amostra'], name='unique_amostra')
                ]

    def __str__(self):
        return self.codigo_amostra +','+ self.metodo_de_coleta +','+ self.material

#Agregado
class Paciente_Exame_Amostra(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    id_exame = models.ForeignKey(Exame, on_delete=models.PROTECT)
    id_amostra = models.ForeignKey(Amostra, on_delete=models.PROTECT)
    data_de_realizacao = models.DateTimeField(auto_now_add=True)
    data_de_solicitacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['id_paciente', 'id_exame', 'id_amostra', 'data_de_realizacao'], name='unique_agreg_exame')
                ]