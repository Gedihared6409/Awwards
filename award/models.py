from django.db import models
from django.contrib.auth.models import User
import datetime as dt 
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    photo=models.ImageField(upload_to='pic/')
    bio=models.TextField()
    username=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    phone_number=models.CharField(max_length=50)
    def save_profile(self):
        self.save()
    def delete_profile(self):
       self.delete()

    def update_bio(self,bio):
         self.bio=bio
         self.save()

