from django.db import models

# Create your models here
class Testes(models.Model):
	name = models.CharField(max_length=50)
	kaqui = models.CharField(max_length=50,default="")