from django.urls import path,include
from .views import BookDetails
urlpatterns = [
    path('book_detail/<int:id>',BookDetails.as_view(),name="book_detail"),
]