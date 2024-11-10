from django.db import models
from catagory.models import Catagory
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=80)
    content=models.TextField()
    catagory=models.ManyToManyField(Catagory)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="post/medias/uploads/",blank=True,null=True)


    def __str__(self):
        return self.title

class Coment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="Comments")
    name=models.CharField(max_length=40)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self.name}"

    
    