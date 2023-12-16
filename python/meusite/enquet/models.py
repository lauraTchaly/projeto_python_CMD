from django.db import models
class Questao(models.Model):
    questao_texto = models.CharField(max_legth=200)
    data_pub = models.DateTimeField("date published")


class Escolha(models.Model):
    questao = models.ForeignKey(Questao,on_delete=models.CASCADE)
    escolha_texto = models.CharField(max_legth=200)
    votos = models.IntegerField(defauld=0)

# Create your models here. ( banco de dados )
