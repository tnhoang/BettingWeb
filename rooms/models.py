from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone


class Room(models.Model):
    user_create     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_create')
    room_name       = models.CharField(max_length=200)
    name_team_A     = models.CharField(max_length=200)
    name_team_B     = models.CharField(max_length=200)
    id_team_a       = models.IntegerField(default=0)
    id_team_b       = models.IntegerField(default=1)
    id_team_win     = models.IntegerField(null=True, blank=True)
    players_team_A  = models.ManyToManyField(User, related_name='player_A')
    players_team_B  = models.ManyToManyField(User, related_name='player_B')
    time_start      = models.DateTimeField(auto_now_add=True)
    time_play       = models.CharField(max_length=10)
    time_end        = models.DateTimeField(null=True, blank=True)
    default_money   = models.IntegerField(default=10)
    max_money       = models.IntegerField(null=True, blank=True)
    max_player      = models.IntegerField(default=16)
    total_player    = models.IntegerField(null=True, blank=True)
    live_url        = models.URLField(max_length=200, null=True, blank=True)
    containner      = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.name_room
    
    def save(self, *args, **kwargs):
        days = self.time_play.split(':')[0]
        hours = self.time_play.split(':')[1]
        minutes = self.time_play.split(':')[2]
        self.time_end = datetime.now(tz=timezone.utc) + timedelta(days=days, hours=hours, minutes=minutes)
        super(Room, self).save(*args, **kwargs)

    @property
    def is_expired(self):
        if datetime.now(tz=timezone.utc) > self.time_end:
            return True
        return False


