from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)



class User(AbstractBaseUser):
    user_name   = models.CharField(max_length=255, blank=True, null=True)
    full_name   = models.CharField(max_length=255, blank=True, null=True)
    email       = models.EmailField(max_length=255, unique=True)
    age         = models.IntegerField()
    birth_day   = models.DateField(null=True, blank=True)
    gender      = models.CharField(max_length=10)

    def __str__(self):
        return self.user_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    list_friend = models.ManyToManyField(User, related_name='list_friend')
    money = models.FloatField()
