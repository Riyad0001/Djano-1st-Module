from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="add_album"),
    path('edit/<int:id>',views.edit_albm,name="edit_album"),
    path('delete/<int:id>',views.delet_albm,name="delete_album"),
]
