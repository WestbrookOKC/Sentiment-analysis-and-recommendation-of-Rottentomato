from django.db import models

class Movie(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    user = models.CharField(max_length=255)
    recommend = models.TextField(max_length=255)
    url = models.CharField(max_length=255)
    movieName = models.CharField(max_length=255)