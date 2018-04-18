from django.db import models
from django.contrib.auth.models import User
from rooms.models import Room


class History(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    mode                = models.IntegerField(default=0)
    room                = models.ForeignKey(Room, on_delete=models.CASCADE)
    status              = models.CharField(max_length=4, default='waiting')
    money_bet_user      = models.IntegerField(default=10)
    money_bet_creator   = models.IntegerField(default=10)
