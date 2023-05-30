from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Shopper(AbstractUser):
    presentation = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='images/avatars/', verbose_name="Image de profil", blank=True)
    def __str__(self):
        return self.username
