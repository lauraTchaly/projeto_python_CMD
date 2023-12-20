import datetime
from django.db import models
from django.utils import timezone
class Questao(models.Model):
    questao_texto = models.CharField(max_length=200)
    data_pub = models.DateTimeField("date published")
    def _str_(self):
        return self.questao_texto
    def publicado_recentemente(self):
        return self.data_pub >= timezone.now() - datetime.timedelta(days=1)
    
 

class Escolha(models.Model):
    questao = models.ForeignKey(Questao,on_delete=models.CASCADE)
    escolha_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    def _str_(self):
        return self.escolha_texto

# Create your models here. ( banco de dados )
