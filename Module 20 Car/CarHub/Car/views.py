from django.shortcuts import render
from . import forms
from . import models
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView,ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
class SignUpForm(CreateView):
    form_class=forms.RegisterForm
    template_name="signup.html"
    success_url=reverse_lazy('homepage')

class PostDetails(DetailView):
    model=models.Car
    pk_url_kwarg = 'id'
    template_name='blog_detail.html'

    def post(self,request,*args,**kwargs):
        comment_form=forms.ComentForm(data=request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.car=post
            new_comment.save()
        return self.get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        post=self.object
        comments=post.comments.all()
        comment_form=forms.ComentForm()

        context['comments']=comments
        context['comments_form']=comment_form
        return context
@login_required()
def buy_now(request, id):
    car = get_object_or_404(models.Car, id=id)

    if car.Quantity > 0:
        car.Quantity -= 1
        car.save()
        models.Buyed.objects.create(user=request.user, car=car)

        messages.success(request, "Car purchased successfully!")
        return redirect('post_detail', id=id)
    else:
        messages.error(request, "Sorry, this car is out of stock.")
        return redirect('post_detail', id=id)


@login_required()  
def change_dat(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.change_data(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Updated Successfully")
                return redirect('profile')
        else:
            form = forms.change_data(instance=request.user)

        return render(request, './edit_profile.html', {'form': form})
    else:
        return redirect('signup')
# @login_required()
# def profile(request):
#     if request.user.is_authenticated:
#         purchases=models.Buyed.objects.filter(user=request.user)
#         return render(request,'profiles.html',{'purchases':purchases})
#     else:
#         return redirect('login')
@method_decorator(login_required,name="dispatch")
class ProfileVie(ListView):
    model=models.Buyed
    template_name="profiles.html"
    context_object_name='purchases'

    def get_queryset(self):
        return models.Buyed.objects.filter(user=self.request.user)
    


    