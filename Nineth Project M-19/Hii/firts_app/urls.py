from django.urls import path
from . import views
urlpatterns = [
    path('',views.set_season ),
    path('cok/',views.get_cookie ),
    path('del/',views.delet_cookie),
    path('dels/',views.delete_session),
    path('sdat/',views.get_season),
]