from django.db import models
class language(models.Model):
	name           = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class profesional(models.Model):
	firstname      = models.CharField(max_length=50)
	lastname       = models.CharField(max_length=50)
	picture        = models.FileField(upload_to='uploads/avatar/', null=True, blank=True)
	languages      = models.ManyToManyField(language)
	def __str__(self):
		return self.firstname + " " + self.lastname
class language_tips(models.Model):
	title          = models.CharField(max_length=250)
	description    = models.TextField()
	language_id    = models.ManyToManyField(language)
	def __str__(self):
		return self.title + " (" + self.language_id.name + ")"
