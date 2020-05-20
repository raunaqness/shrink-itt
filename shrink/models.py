from django.db import models

# Create your models here.

class URLs(models.Model):
	shrinked_url = models.CharField(primary_key=True, db_index=True, unique=True, max_length=8)
	complete_url = models.CharField(max_length=2048)
	created = models.DateTimeField(auto_now_add=True, blank=True)
	visited_count = models.IntegerField(default=0)