from django.db import models

# Create your models here.
class Paciente(models.Model):
	#id = models.IntegerField(primary_key=True)
	dni = models.CharField(max_length=50)
	nombres= models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
