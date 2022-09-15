from operator import mod
from turtle import title
from django.db import models
from django.contrib.auth.models import User

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

## blog ##

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    