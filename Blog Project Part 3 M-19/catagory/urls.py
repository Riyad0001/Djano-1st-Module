from django.urls import path,include
from . import views
urlpatterns = [
    path('catagory',views.add_catagory,name="add_catagory"),
    path('edit/<int:id>',views.edit_cat,name="edit_catagory"),
    path('delete/<int:id>',views.delet_post,name="delete_catagory"),
]
