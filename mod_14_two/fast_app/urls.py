from django.urls import path,include
from fast_app.views import home
urlpatterns = [
    path('',home,name="homepage"),
]