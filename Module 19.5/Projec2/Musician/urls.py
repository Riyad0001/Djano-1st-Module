from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('add_musician',views.AddMusiView.as_view(),name="add_musi"),
    path('edit_musician/<int:id>',views.EditMusi.as_view(),name="edit_musi"),
    path('login/',LoginView.as_view(template_name="login.html"),name="login"),
    path('logout/',LogoutView.as_view(next_page='/homepage/'),name="logout"),
    path('signup/',views.SignupView.as_view(),name="signup"),
]