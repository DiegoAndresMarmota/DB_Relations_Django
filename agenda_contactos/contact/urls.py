from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="contact"),
    path("view/<int:id>", views.view, name="contact_view")    
]
