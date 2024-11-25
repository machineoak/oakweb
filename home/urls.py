from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("html", views.index, name="html")
]