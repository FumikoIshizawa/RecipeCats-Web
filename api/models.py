from django.db import models
import enum

class Category(enum.IntEnum):
	MainDish = 0
	SubDish = 1
	Food = 2
	Soup = 3

class Recipe(models.Model):
	title = models.CharField(max_length=100)
	url = models.URLField()
	category = models.IntegerField(default=0)
