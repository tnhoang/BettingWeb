from django import forms
from django.forms import ModelForm
from .models import Room

class RoomCreation(forms.ModelForm):
    class Meta:
        model   = Room
        fields  = ['room_name', 'name_team_A', 'name_team_B', 'default_money', 'max_player', 'time_play',]  

class UpdateTeamWin(forms.Form):
    id_team_win = forms.IntegerField()
