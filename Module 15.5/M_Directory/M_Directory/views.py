from django.shortcuts import render
from albums.models import Album
# Create your views here.
def homes(request):
    data=Album.objects.all()
    return render(request,'home.html',{'data':data})