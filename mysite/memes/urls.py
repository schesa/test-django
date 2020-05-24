from django.urls import path

from . import views

urlpatterns = [
    path("memes", views.memes, name="memes"),
]