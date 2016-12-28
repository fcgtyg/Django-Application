from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from tags.models import Tag
from .models import Blog
from .forms import BlogForm

def show_entries(request):

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.owner = request.user
            entry.save()
            form.save_m2m()

    elif request.method == "GET":
        form = BlogForm()

    return render(request, "my_entries.html", {"entries": Blog.objects.filter(owner=request.user.id),
                                               "tags":Tag.objects.all(),
                                               "form": form})


def get_entry(request, entry_id):
    try:
        entry = Blog.objects.get(id=entry_id)
        if request.user.id != entry.owner.id:
            raise PermissionDenied
        return render(request, "entry_detail.html", {"entry": entry})
    except Blog.DoesNotExist:
        raise Http404("We don't have any.")
