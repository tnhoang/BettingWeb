from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name       = models.CharField(max_length=255)
    gender          = models.CharField(max_length=255)
    birth_day       = models.DateField(auto_now=False, auto_now_add=False)
    finance         = models.IntegerField(default=50)
    list_friend     = models.ManyToManyField(User, related_name='list_friend')
