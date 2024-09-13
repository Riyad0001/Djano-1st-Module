
from django.urls import path,include
from . import views
urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('profile/',views.profile,name="profile"),
    path('change_password/',views.change_pass,name="cng_pass"),
    path('change_password2/',views.change_pass2,name="cng_pass2"),
]