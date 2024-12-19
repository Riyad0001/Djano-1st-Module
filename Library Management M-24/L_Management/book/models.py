from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):  
    name = models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,blank=True,null=True,unique=True)

    def __str__(self):
        return self.name


class Book(models.Model): 
    title = models.CharField(max_length=80)
    description = models.TextField()
    borrowing_price=models.IntegerField(blank=True,null=True)
    category = models.ManyToManyField(Category)  
    image = models.ImageField(upload_to="book/medias/uploads/", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title'] 


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=40)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} on {self.book.title}"

    class Meta:
        ordering = ['-created_on'] 
