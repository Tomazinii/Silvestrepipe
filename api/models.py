from django.db import models

# Create your models here
class Testes(models.Model):
	name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50,default="")
	kaqui = models.CharField(max_length=50,default="")
	alecrin = models.CharField(max_length=50,default="")


	def __str__(self):
		return self.name
	