from django.db import models
from django.contrib.auth.models import User


class SeriesName(models.Model):
    createName = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='app/static/photos/icons')

    def __str__(self):
        return self.createName



class CharacterInfo(models.Model):
    seriesName = models.ForeignKey(SeriesName, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    planet = models.CharField(max_length=255)
    quote = models.CharField(max_length=255)
    image = models.ImageField(upload_to ='app/static/photos')
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



class UserSeries(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    createName = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='app/static/photos/icons')

    def __str__(self):
        return self.createName


class UserCharacter(models.Model):
    seriesName = models.ForeignKey(UserSeries, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    planet = models.CharField(max_length=255)
    quote = models.CharField(max_length=255)
    image = models.ImageField(upload_to ='app/static/photos')
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


