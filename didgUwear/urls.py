from django.urls import path
from didgUwear import views


urlpatterns = [
    path("", views.home, name="home"),
    path("shirts", views.shirts, name="shirts"),
    path("pants", views.pants, name="pants"),
    path("closet", views.closet, name="closet"),
    path("add", views.add, name="add"),
]
