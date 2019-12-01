from django.urls import path
from didgUwear import views


urlpatterns = [
    path("", views.closet, name="home"),
    path("shirts", views.shirts, name="shirts"),
    path("pants", views.pants, name="pants"),
    path("closet", views.closet, name="closet"),
    path("add", views.add, name="add"),
    path("style", views.style, name="style"),
    path("styleinput/<path:input>", views.StyleInput.as_view(), name="styleInput")
]
