from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import RegisterForm
from .models import UserDetail

User = get_user_model()
def register_view(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username    = form.cleaned_data.get('username')
        email       = form.cleaned_data.get('email')
        password    = form.cleaned_data.get('password1')
        User.objects.create(username=username, email=email, password=password)
        UserDetail.objects.create(user=User.objects.get(username=username), finance=50)
        return redirect("/hello")
    return render(request, "accounts/register.html", context)

def test_view(request):
    print(User.objects.get(username='user2').userdetail.finance)
    return render(request,'accounts/test.html')
