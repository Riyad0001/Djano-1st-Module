from django.urls import path,include
from . import views
urlpatterns = [
    path('add_post/',views.addPostClass.as_view(),name="add_post"),
    # path('add_post/',views.add_post,name="add_post"),
    # path('edit/<int:id>',views.edit_post,name="edit_post"),
    path('edit/<int:id>',views.EditPostView.as_view(),name="edit_post"),
    path('delete/<int:id>',views.DeletPostView.as_view(),name="delet_post"),
    path('post_detail/<int:id>',views.PostDetails.as_view(),name="post_detail"),
    # path('delete/<int:id>',views.delet_post,name="delet_post"),
]
