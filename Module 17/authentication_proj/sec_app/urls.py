from django.urls import path
from . import views
urlpatterns = [
    path('/signup',views.signup,name="signup"),
    path('',views.home,name="homepage"),
    path('/profile',views.profile,name="profile"),
    path('/login',views.login_page,name="login"),
    path('/loged_out',views.loged_out,name="logout"),
    path('/change_password',views.change_pass,name="pass_cng"),
    path('/change_password2',views.change_pass2,name="pass_cng2"),
    path('/change_userdata',views.change_dat,name="data_cng"),
]
