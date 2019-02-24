from django.db import models

# Create your models here.

class Resume(models.Model):
	"""docstring for resume"""
	label = models.CharField(max_length=200)

	def __str__(self):
		return self.label


class Fieldset(models.Model):
	"""docstring for Fieldset"""
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	label = models.CharField(max_length=200)
	position = models.IntegerField()
	
	def __str__(self):
		return self.label


class Field(models.Model):
	"""docstring for Fieldset"""
	fieldset = models.ForeignKey(Fieldset, on_delete=models.CASCADE)
	label = models.CharField(max_length=200)
	text = models.TextField()
	position = models.IntegerField()

	def __str__(self):
		return self.label

class ImageField(models.Model):
	"""docstring for Fieldset"""
	fieldset = models.ForeignKey(Fieldset, on_delete=models.CASCADE)
	label = models.CharField(max_length=200)
	text = models.TextField()
	image = models.ImageField(upload_to='images')
	position = models.IntegerField()

	def __str__(self):
		return self.label