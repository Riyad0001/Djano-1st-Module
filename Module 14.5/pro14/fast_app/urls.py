from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.homeView),
    path('1',views.modelView),
]
