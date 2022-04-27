from distutils.command.upload import upload
from pyexpat import model
from turtle import update
from django.db import models

# Create your models here.

class Tempuser(models.Model):
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=32)


class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(blank=True, null=True)
    head_image = models.ImageField(
        upload_to = 'landing/images/%Y/%m/%d/%H/',
        blank = True
    )
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(
            Tempuser, 
            on_delete=models.CASCADE,
            blank=True, null = True
            )
    liked_users = models.ManyToManyField(
        Tempuser,
        related_name='user_likes'
    )

    

    
