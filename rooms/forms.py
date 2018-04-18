from django import forms
from django.forms import ModelForm
from .models import Room

class RoomCreation(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model   = Room
        fields  = ['name_room', 'password', 'name_team_A', 'name_team_B', 'max_player', 'time_play',]  

class UpdateTeamWin(forms.Form):
    id_team_win = forms.IntegerField()
