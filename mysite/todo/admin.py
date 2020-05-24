from django.contrib import admin

from todo.models import Todo
from memes.models import Meme
# Register your models here.

admin.site.register(Todo)
admin.site.register(Meme)