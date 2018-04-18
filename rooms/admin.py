from django.contrib import admin
from .models import Room, Detail, Enrollment


#class RoomAdmin(admin.ModelAdmin):
#   list_display = ('name', 'description', 'time_start', 'time_end', 'default_money', 'creator')


#class EnrollmentAdmin(admin.ModelAdmin):
#    list_display = ('room', 'user', 'team_choose', 'money_to_bet')


#class DetailAdmin(admin.ModelAdmin):
#    list_display = ('room', 'still_open', 'name_team_A', 'name_team_B')
admin.site.register(Room)
admin.site.register(Detail)
admin.site.register(Enrollment)


