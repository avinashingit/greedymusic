from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Track(models.Model):
	title = models.CharField(max_length=50)
	genre = models.CharField(max_length=50)
	rating = models.IntegerField(default=0)

	def __str__(self):
		return self.title


class Genre(models.Model):
	#track = models.ForeignKey(Track, on_delete=models.CASCADE)
	genre_name = models.CharField(max_length=50)

	def __str__(self):
		return self.genre_name