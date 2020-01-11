from django.urls import path
from didgUwear import views


urlpatterns = [
    path("", views.closet, name="home"),
    path("shirts", views.shirts, name="shirts"),
    path("pants", views.pants, name="pants"),
    path("closet", views.closet, name="closet"),
    path("addShirt", views.AddShirt.as_view(), name="addShirt"),
    path("addPant", views.AddPant.as_view(), name="addPant"),
    path("style", views.style, name="style"),
    path("styleinput/<path:input>", views.StyleInput.as_view(), name="styleInput"),
    path("addinputshirt", views.addInputShirt.as_view(), name="addinputshirt"),
    path("addinputpant", views.addInputPant.as_view(), name="addinputpant"),
    path("deleteitem/<path:nickname>/<path:clothing>", views.DeleteItem.as_view(), name="deleteItem"),
    path("findprediction", views.FindPrediction.as_view(), name="findPrediction"),
    path("predictions", views.Prediction.as_view(), name="predictions")
]
