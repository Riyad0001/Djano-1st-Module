from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_profile(request):
    if request.method=="POST":
        add_profiles=forms.ProfileFr(request.POST)
        if add_profiles.is_valid:
            add_profiles.save(commit=True)
            return redirect('add_profile')
    else:
        add_profiles=forms.ProfileFr()
    return render(request,"add_profile.html",{'form':add_profiles})