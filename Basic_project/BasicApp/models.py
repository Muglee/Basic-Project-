from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    USER =[
        ('admin','Admin'),
        ('viewer','Viewer'),
    ]
    user_type=models.CharField(choices=USER,max_length=10)
    
class adminProfileMOdel(models.Model):
    
    user=models.OneToOneField(customUser,on_delete=models.CASCADE,related_name='adminProfile')
    
    def __str__(self):
        return f'{self.user.username}'
    
class viewerProfileMOdel(models.Model):
    
    user=models.OneToOneField(customUser,on_delete=models.CASCADE,related_name='viewerProfile')
    
    def __str__(self):
        return f'{self.user.username}'
    
