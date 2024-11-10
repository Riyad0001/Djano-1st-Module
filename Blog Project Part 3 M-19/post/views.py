from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.
# @login_required()
# def add_post(request):
#     if request.method=="POST":
#         PoForm=forms.PostForm(request.POST)
#         if PoForm.is_valid:
#             # PoForm.cleaned_data['author']=request.user
#             PoForm.instance.author=request.user
#             PoForm.save(commit=True)
#             return redirect('add_post')
#     else:
#         PoForm=forms.PostForm()
#     return render(request,"add_post.html",{"form":PoForm})

# class based view 
@method_decorator(login_required,name="dispatch")
class addPostClass(CreateView):
    model=models.Post
    form_class=forms.PostForm
    template_name="add_post.html"
    success_url=reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


@login_required()
def edit_post(request,id):
    post=models.Post.objects.get(pk=id)
    PoForm=forms.PostForm(instance=post)
    if request.method=="POST":
        PoForm=forms.PostForm(request.POST,instance=post)
        if PoForm.is_valid:
            PoForm.instance.author=request.user
            PoForm.save(commit=True)
            return redirect('homepage')
    return render(request,"add_post.html",{"form":PoForm})
@method_decorator(login_required,name="dispatch")
class EditPostView(UpdateView):
    model=models.Post
    form_class=forms.PostForm
    template_name="add_post.html"
    success_url=reverse_lazy('profile')
    pk_url_kwarg="id"
@method_decorator(login_required,name="dispatch")
class DeletPostView(DeleteView):
    model=models.Post
    template_name="delete.html"
    success_url=reverse_lazy('profile')
    pk_url_kwarg="id"

@login_required()
def delet_post(request,id):
    post=models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
class PostDetails(DetailView):
    model=models.Post
    pk_url_kwarg = 'id'
    template_name='blog_detail.html'

    def post(self,request,*args,**kwargs):
        comment_form=forms.ComentForm(data=self.request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
        return self.get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        post=self.object
        comments=post.Comments.all()
        comment_form=forms.ComentForm()

        context['comments']=comments
        context['comments_form']=comment_form
        return context

    