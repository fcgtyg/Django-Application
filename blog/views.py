from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import all_entries

from users.models import Logged_user
# Create your views here.

def show_entries(request):
    user = Logged_user["active"]
    return render(request, "blog_entries.html", {"Entries": all_entries, "username" : user})

def get_entries(request, todo_id):
    user = Logged_user["active"]
    try:
        return HttpResponse("<p1>" + "Hi, again " + user + "</p1>" + "<h1>" + all_entries[int(todo_id)][0] + "</h1>" + "<br/>" + "<p1>" + all_entries[int(todo_id)][1] + "</p1>")
    except IndexError:
        raise Http404("We don't have any.")
