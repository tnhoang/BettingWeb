from django.contrib import admin
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_name',  'time_start', 'time_play', 'time_end', 'default_money', 'user_create')


#class EnrollmentAdmin(admin.ModelAdmin):
#    list_display = ('room', 'user', 'team_choose', 'money_to_bet')


#class DetailAdmin(admin.ModelAdmin):
#    list_display = ('room', 'still_open', 'name_team_A', 'name_team_B')
admin.site.register(Room, RoomAdmin)


