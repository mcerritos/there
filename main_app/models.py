from django.db import models

# Create your models here.
class Cryptid(models.Model):
	name = models.CharField(max_length=100)
	region = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	danger_level = models.IntegerField()

	#overwrite __str__

	def __str__(self):
		return self.name

class Sighting(models.Model):
	date = models.DateField('Date of sighting')
	location = models.CharField(max_length=100)
	description = models.TextField(max_length=500)

	cryptid = models.ForeignKey(Cryptid, on_delete=models.CASCADE)

