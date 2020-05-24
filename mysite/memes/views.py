from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Todo
import os

# Create your views here.
def memes(request):
    "Memes"
    # return HttpResponse(content="Memes!")
    path = os.getcwd()
    return render(request, 'memes/memes-list.html', {})
