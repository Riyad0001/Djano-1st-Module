from django.urls import path,include
from . import views

urlpatterns = [
    path('add_task/',views.add_task,name="add_task"),
]