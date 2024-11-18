from django.views.generic.edit import CreateView
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
@method_decorator(login_required, name='dispatch')
class AddAlbum(CreateView,SuccessMessageMixin):
    template_name = "add_album.html"
    form_class = forms.AlbumForm
    success_url = reverse_lazy("homepage")
    model = models.Album
    success_message="Album Created Sucessfully"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
@method_decorator(login_required, name='dispatch')
class EditAlbum(UpdateView,SuccessMessageMixin):
    template_name="add_album.html"
    success_url=reverse_lazy("homepage")
    model=models.Album
    form_class=forms.AlbumForm
    pk_url_kwarg="id"
    success_message="Album Updated Sucessfully"
@method_decorator(login_required, name='dispatch')
class DeleteAlbum(DeleteView):
    template_name="delete_albm.html"
    success_url=reverse_lazy("homepage")
    model=models.Album
    pk_url_kwarg="id"

    
