from django.db import models

# Create your models here.
class Score(models.Model):
	score = models.IntegerField()
	time = models.DateTimeField()
	location = models.IntegerField()