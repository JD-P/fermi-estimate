from django.db import models

# Create your models here.

#Fermi estimate Question class - stores question and real answer to given fermi estimate question.
#models.FloatField is used because answers are assumed to be in the form of a number

class Question (models.Model):
	question = models.TextField()
	answer = models.FloatField()

#Fermi estimate Estimate class - stores user estimate, the time the question was presented to the user and the time it took for the user to provide an estimate.

class Estimate(models.Model):
	question = models.ForeignKey(Question)
	estimate = models.FloatField()
	time_posed = models.DateTimeField(Question)
	time_answered = models.DateTimeField(Estimate)
