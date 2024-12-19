from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Review,Book
from django.views.generic import DetailView
from .forms import ReviewForm
from django.contrib import messages
# Create your views here.

class BookDetails(DetailView):
    model=Book
    pk_url_kwarg = 'id'
    template_name='book_detail.html'

    def post(self,request,*args,**kwargs):
        review_form=ReviewForm(data=self.request.POST)
        book=self.get_object()
        existing_review = Review.objects.filter(book=book, email=review_form.data.get('email')).first()

        if existing_review:
            messages.error(request, "You have already submitted a review for this book.")
            return redirect(reverse('book_detail', kwargs={'id': book.id}))
        if review_form.is_valid():
            new_review=review_form.save(commit=False)
            new_review.book=book
            new_review.save()
            messages.success(request, "Your review has been submitted successfully.")
            return redirect(reverse('book_detail', kwargs={'id': book.id}))
        return self.get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        post=self.object
        comments=post.reviews.all()
        review_form=ReviewForm()

        context['comments']=comments
        context['reviews_form']=review_form
        return context
