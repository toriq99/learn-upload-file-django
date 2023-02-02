from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MyForm
from .models import Review

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST)

        if form.is_valid():
            review = Review(
                user_name = form.cleaned_data['user_name'],
                review_text = form.cleaned_data['review_text'],
                rating = form.cleaned_data['rating']
            )
            review.save()

            return HttpResponseRedirect('/thank-you')        
    else:
        form = MyForm()

    return render(request,'reviews/reviews.html', {
        'form': form
    })


def thankyou(request):
    form = Review.objects.all() 
    latest_username = Review.objects.latest('user_name') # get latest index selected column
    return render(request, 'reviews/thank_you.html',{
        'latest_username' : latest_username.user_name  # select lastest 'user_name'
    })