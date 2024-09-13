from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.registerForm,name="register"),
    path('login/',views.LoginForm,name="login"),
    path('logout/',views.logedOut,name="logout"),
    path('edit_profile/',views.ProfileEdt,name="edt_profile"),
    path('profile/',views.Profile,name="profile"),
    path('change_passs/',views.Cng_Pass,name="cng_pass"),
]


