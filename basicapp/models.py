from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):

    def __str__(self):
        return self.p_name
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1, related_name='products')
    p_name=models.CharField(max_length=50)
    p_desc=models.CharField(max_length=500)
    p_date=models.DateField(auto_now_add=True)
    p_price=models.IntegerField()
    p_image=models.ImageField(upload_to="basicapp/images",default="basicapp/images/placeholder.png")

    
