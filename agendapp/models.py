from __future__ import unicode_literals

from django.db import models
class Contato(models.Model):
	nome = models.CharField(max_length=200)
	telefone1 = models.CharField(max_length=20)
	telefone2 = models.CharField(max_length=20,blank=True)
	email = models.CharField(max_length=100)
	endereco = models.TextField(blank=True)
	dtnasc = models.DateField()
	obs = models.TextField(blank=True)
