from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name       = models.CharField(max_length=255)
    gender          = models.CharField(max_length=255)
    birth_day       = models.DateField(auto_now=False, auto_now_add=False)
    money           = models.FloatField(default=50.0)

    def __str__(self):
        return self.full_name


class ListFriend(models.Model):
    user            = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user')
    friend_list     = models.ManyToManyField(User, related_name='friend_list')


class History(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_history')
#   room            = models.ForeignKey(Room, related_name='room_history')
    win_status      = models.BooleanField(default=False)
    money_bet       = models.FloatField(null=True)
    def __str__(self):
        return self.user
