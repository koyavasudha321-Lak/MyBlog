from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Category(models.Model):
   name = models.CharField(max_length=255,default='Unknown')
   created = models.DateTimeField(default=datetime.now)

   def __str__(self):
      return self.name

   class Meta:
      verbose_name = 'Category'
      verbose_name_plural = 'Categories'


class Post(models.Model):
   category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='categories')
   user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='users')
   title = models.CharField(max_length=255)
   thumbnail = models.ImageField(upload_to='post/thumbnail')
   description = models.TextField()
   tags = models.CharField(max_length=255)
   posted_at = models.DateField(default=datetime.now)
   is_published = models.BooleanField(default=False)


   class Meta: 
     verbose_name = ("Post")
     verbose_name_plural = ("Posts")

   def __str__(self):
      return self.title