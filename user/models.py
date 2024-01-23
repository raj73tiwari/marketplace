from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    def __str__(self):
        return self.user.username
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    about=models.CharField(max_length=500)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to="user/profile-pic",default="user/profile-pic/defaultpic.png")
