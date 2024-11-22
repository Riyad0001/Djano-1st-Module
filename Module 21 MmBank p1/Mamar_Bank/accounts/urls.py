from .views import RegFormView,LoginVieww,LgOutview
from django.urls import path,include

urlpatterns = [
    path('register/',RegFormView.as_view(),name="register"),
    path('login/',LoginVieww.as_view(),name="login"),
    path('logout/',LgOutview.as_view(),name="logout"),
]
