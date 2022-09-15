from operator import mod
from turtle import title
from django.db import models

# Create your models here.

class Latestnews(models.Model):
    title = models.CharField( max_length=100)
    file = models.FileField(upload_to='news', max_length=100)
    link = models.URLField(max_length=200, null=True)
    pub_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.title


class Slider(models.Model):
    altText = models.CharField(max_length=50)
    image = models.ImageField(upload_to='slider',max_length=100)
    url = models.URLField(max_length=200)
    pub_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.altText

class Places(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider',max_length=100)
    altText = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    about = models.TextField()
    pub_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.title

class Authorities(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='slider',max_length=100)
    DESIG_CHOICES = (
        ('Mukhiya', 'Mukhiya'),
        ('Up Mukhiya', 'Up Mukhiya'),
        ('Sarpanch', 'Sarpanch'),
        ('Up Sarpanch', 'Up Sarpanch'),
        ('Panchayat Samiti', 'Panchayat Samiti'),
        ('Ward Member', 'Ward Member'),
    )
    designation = models.CharField(max_length=50, choices=DESIG_CHOICES)
    about = models.TextField(blank=True)
    pub_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.name

    