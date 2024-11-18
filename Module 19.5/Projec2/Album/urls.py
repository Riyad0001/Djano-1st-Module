from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('add_album/',views.AddAlbum.as_view(),name="add_album"),
    path('edit_album/<int:id>',views.EditAlbum.as_view(),name="edit_album"),
    path('delete_album/<int:id>',views.DeleteAlbum.as_view(),name="delete_album"),
]