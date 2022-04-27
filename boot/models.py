from django.db import models

# Create your models here.
class Inquiry(models.Model):
    fullname = models.CharField(max_length=64, blank = True, null = True)
    email = models.CharField(max_length=64, blank = True, null = True)
    phone_number = models.CharField(max_length=32, blank = True, null = True)
    message = models.TextField(blank = True, null = True)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)


# class Login(models.Model):
