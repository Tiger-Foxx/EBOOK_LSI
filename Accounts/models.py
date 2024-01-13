from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import AbstractUser,User
from regex import M

# Create your models here.
class Utilisateur(AbstractUser):
    email=models.EmailField(unique=True)
    username = models.CharField(max_length=125,unique=True)
    password = models.CharField(max_length=300)
    telephone = models.CharField(max_length=9)
    profil=models.ImageField(upload_to="Photos de Profile")
    is_premium=models.BooleanField(null=True,blank=True,default=False)
    is_premium=models.BooleanField(default=False)
    def __str__(self):
        return f" Utilisateur | nom: {self.username} | email: {self.email}"