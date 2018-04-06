from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import RegisterForm

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
    return render(request, "accounts/register.html", context)

