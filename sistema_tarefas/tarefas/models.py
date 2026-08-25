from django.db import models

# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    concluida = models.BooleanField()
    data = models.DateField()
    prioridade = models.IntegerField(choices=[
    (1, "Baixa"),
    (2, "Média"),
    (3, "Alta"),
])