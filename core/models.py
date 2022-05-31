import email
from django.db import models

# Create your models here.
class Aluno (models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    telefone = models.CharField(max_length=100)
