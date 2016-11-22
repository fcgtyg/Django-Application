from django.shortcuts import render, HttpResponse
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import all_entries
# Create your views here.

def show_entries(request):
    return render(request, "blog_entries.html", {"Entries": all_entries})

def get_entries(request, todo_id):
    try:
        return HttpResponse("<h1>" + all_entries[int(todo_id)][0] + "</h1>" + "<br/>" + "<p1>" + all_entries[int(todo_id)][1] + "</p1>")
    except IndexError:
        raise Http404("We don't have any.")
