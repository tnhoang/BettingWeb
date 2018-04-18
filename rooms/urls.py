from django.urls import path
from . import views


app_name='rooms'

urlpatterns = [
    path('',views.List_Room.as_view(), name='list_room'),
    path('create',views.create_room, name='create_room'),
    path('<int:pk>',views.Detail_Room.as_view(), name='detail_room'),
    path('<int:pk>/edit',views.update_team_win, name='edit_room'),
]
