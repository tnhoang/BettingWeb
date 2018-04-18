from django.shortcuts import render, redirect,get_object_or_404
from  .forms import RoomCreation, UpdateTeamWin
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from .models import Room, Detail
from django.views import generic
from accounts.models import UserDetail
def create_room(request):
    user = User.objects.first()
    form = RoomCreation(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        name_room       = form.cleaned_data.get('name_room')
        name_team_A       = form.cleaned_data.get('name_team_A')
        name_team_B       = form.cleaned_data.get('name_team_B')
        time_play       = form.cleaned_data.get('time_play')
        max_player       = form.cleaned_data.get('max_player')
        room = Room.objects.create(
                name_room = name_room,
                name_team_A = name_team_A,
                name_team_B = name_team_B,
                time_play = time_play,
                max_player = max_player,
                user_create = user)
        return redirect('/admin/rooms/room/')
    return render(request, 'rooms/create_room.html', context)


class List_Room(generic.ListView):
    model = Room
    fields = ['id_team_win']
    template_name = 'rooms/list_room.html'




class Detail_Room(generic.DetailView):
    model = Room
    template_name = 'rooms/detail_room.html'
    context_object_name = 'room'


def update_team_win(request, pk):
    form = UpdateTeamWin(request.POST or None)
    context = {
            'form':form
            }
    if form.is_valid():
        room = Room.objects.get(pk=pk)
        room.id_team_win = form.cleaned_data.get('id_team_win')
        if room.id_team_win == 0:
            for user in room.player_team_A.all():
                print(user.id)
                user_detail = UserDetail.objects.get(id=user.id)
                user_detail.money += room.Default_money
                user_detail.save()
        else:
            for user in room.player_team_B.all():
                print(user.id)
                user_detail = UserDetail.objects.get(id=user.id)
                user_detail.money += room.detail.Default_money
                user_detail.save()
        room.save()
        
        return redirect('/hehe')
    return render(request, 'rooms/edit_room.html', context)
#def list_room(request,pk):
#    all_room = get_objects_or_404(Room)
#    render(request, 'rooms/list_room.html', {'all_room':all_room})
