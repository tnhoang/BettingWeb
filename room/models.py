from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Room(models.Model):
    name            = models.CharField(max_length=255)
    description     = models.CharField(max_length=255)
    time_start      = models.DateTimeField(auto_now_add=True)
    time_end        = models.DateTimeField(null=True, blank=True)
    time_play       = models.IntegerField()
    id_team_a       = False
    id_team_b       = True
    id_team_win     = models.BooleanField()
    creator         = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name



#class RoomDetail(models.Model):
#    room            = models.OneToOneField(Room)


