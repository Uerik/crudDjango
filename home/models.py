from django.db import models

# Create your models here.
class Basico(models.Model):
  nome = models.CharField(max_length=50)
  telefone = models.CharField(max_length=12)

  def __str__(self):
    return f"{self.nome} {self.telefone}"