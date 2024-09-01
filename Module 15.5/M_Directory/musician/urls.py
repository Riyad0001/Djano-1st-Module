from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.add_Musi,name="add_musician"),
    path('edit/<int:id>',views.edit_musi,name="edit_musi"),
]
