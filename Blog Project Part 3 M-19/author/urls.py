from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',views.registerForm,name="register"),
    path('login/',views.UserLoginView.as_view(),name="login"),
    # path('login/',views.LoginForm,name="login"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    # path('logout/',views.logedOut,name="logout"),
    path('edit_profile/',views.ProfileEdt,name="edt_profile"),
    path('profile/',views.Profile,name="profile"),
    path('change_passs/',views.Cng_Pass,name="cng_pass"),
]


