from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('delet/<int:roll>',views.delet_student,name="delet_stu"),
]
