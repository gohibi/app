from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to="users-profile/", blank=True, null=True , verbose_name="photo profil")
    
    class Meta:
        verbose_name_plural = "Users"
        db_table = "User"
    
    def __str__(self):
        return self.username