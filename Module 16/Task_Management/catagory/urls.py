from django.urls import path,include
from . import views

urlpatterns = [
    path('add_cat/',views.add_cat,name="add_cat"),
]