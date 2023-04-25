from django.db import models

# Create your models here.
class RegisteredUser(models.Model):
    user_name = models.CharField(max_length=200, verbose_name='first name')
    password = models.CharField(max_length=200, verbose_name='password')
    
    def __str__(self):
        return self.user_name
    