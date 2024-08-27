
from django.urls import path
from . import views
urlpatterns = [
    path('add_meal/',views.add_meals,name="add_meal"),
]

