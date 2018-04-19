from django.shortcuts import render, redirect,get_object_or_404
from  .forms import RoomCreation, UpdateTeamWin
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from .models import Room
from django.views import generic
from accounts.models import UserDetail
def pay_money(user, room):
    pass

def create_room(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        form = RoomCreation(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            room_name       = form.cleaned_data.get('room_name')
            name_team_A     = form.cleaned_data.get('name_team_A')
            name_team_B     = form.cleaned_data.get('name_team_B')
            default_money   = form.cleaned_data.get('default_money')
            time_play       = form.cleaned_data.get('time_play')
            max_player      = form.cleaned_data.get('max_player')
            if user.userdetail.finance < default_money * max_player:
                return render(request, "rooms/not_enough_money.html") 
            else:
                container = default_money * max_player 
                userdetail = UserDetail.objects.get(user=user)
                userdetail.finance -= container
                userdetail.save()
                Room.objects.create(
                    room_name=room_name,
                    name_team_A=name_team_A,
                    name_team_B=name_team_B,
                    time_play=time_play,
                    max_player=max_player,
                    user_create=user,
                    container=container)
            return redirect('/admin/rooms/room/')
        return render(request, 'rooms/create_room.html', context)


class List_Room(generic.ListView):
    model = Room
    fields = ['id_team_win']
    template_name = 'rooms/list_room.html'
    context_object_name = 'all_room'



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
        room = Room.objects.get(id=pk)
        room.id_team_win = form.cleaned_data.get('id_team_win')
        if room.id_team_win == 0:
            for user in room.players_team_A.all():
                money_each_user_get = room.default_money *2
                room.container -= money_each_user_get
                user_detail = UserDetail.objects.get(user=user)
                user_detail.finance += money_each_user_get
                user_detail.save()
            money_creator_get = room.container
            user_who_create_room = UserDetail.objects.get(user=room.user_create)
            user_who_create_room.finance += money_creator_get
            user_who_create_room.save() 
        else:
            for user in room.players_team_A.all():
                money_each_user_get = room.default_money *2
                room.container -= money_each_user_get
                user_detail = UserDetail.objects.get(user=user)
                user_detail.finance += money_each_user_get
                user_detail.save()
            money_creator_get = room.container
            user_who_create_room = UserDetail.objects.get(user=room.user_create)
            user_who_create_room.finance += money_creator_get
            user_who_create_room.save() 
        return redirect('/hehe')
    return render(request, 'rooms/edit_room.html', context)
#def list_room(request,pk):
#    all_room = get_objects_or_404(Room)
#    render(request, 'rooms/list_room.html', {'all_room':all_room})
