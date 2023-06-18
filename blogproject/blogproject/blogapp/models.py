from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    author = models.CharField(max_length=255,blank=True,null=True)
    message = models.TextField(blank=True,null=True)

