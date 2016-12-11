from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Logged_user

from django.contrib.auth.models import User

# Create your views here.
def signup(request):

    if request.method == "POST":

        User.objects.create_user(username=request.POST.get("username"),
                            password=request.POST.get("password"))
        return HttpResponse("Success!")

    return render(request, "register.html")

def username(request):
    user = request.POST.get("username")
    Logged_user["active"] = user
    return user

def login(request):

    if request.method == "POST":
        user = username(request)
        password = request.POST.get("password")

        try:
            user = User.objects.get_by_natural_key(user)
        except:
            return HttpResponse("No such user")

        if User.check_password(user, password):

            return HttpResponseRedirect("/blog/entries/")

        else:
            return HttpResponse("Wrong username or password")

    return render(request, "login.html")
