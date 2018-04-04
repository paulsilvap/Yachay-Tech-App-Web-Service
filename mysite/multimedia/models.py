from django.db import models

# Create your models here.

class File(models.Model):
	name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	image_description = models.TextField()

	def __str__(self):
		return self.name
	def was_published(self):
		return self.pub_date	
	def __str__(self):
		return self.image_description
	class Meta:
		ordering = ('pub_date',)
