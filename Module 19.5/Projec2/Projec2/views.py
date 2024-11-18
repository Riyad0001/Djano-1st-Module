from django.shortcuts import render
from Musician.models import Musi
from Album.models import Album
def home(request):
    # data=Musi.objects.first()
    albm=Album.objects.select_related('Musician').all()
    return render(request,'home.html',{'albm':albm})
