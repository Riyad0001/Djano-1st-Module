from django.shortcuts import render
from .forms import UserRegisterForm
# Create your views here.
from django.views.generic.edit import CreateView

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'users/register.html'
  success_url = reverse_lazy('login')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"
