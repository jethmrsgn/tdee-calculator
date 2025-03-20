from django.db import models

# Create your models here.

class ActivityLevel(models.Model):
	value = models.FloatField()
	description = models.CharField(max_length=150)

	def __str__(self):
		return self.description

class UserHistory(models.Model):
	user = models.CharField(max_length=50)
	gender = models.CharField(max_length=50)
	age = models.IntegerField(default=0)
	weight = models.FloatField()
	height = models.FloatField()
	activity_level = models.ForeignKey(ActivityLevel, on_delete=models.CASCADE)
	macros = models.TextField(default="")
	updated = models.DateField(auto_now=True)

	def __str__(self):
		return self.user
