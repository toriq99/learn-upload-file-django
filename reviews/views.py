from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MyForm
from .models import Review
from django.views import View

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = MyForm()
        
        return render(request,'reviews/reviews.html', {
        'form': form
        })

    def post(self, request):
        form = MyForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')


def thankyou(request):
    form = Review.objects.all() 
    latest_username = Review.objects.latest('user_name') # get latest index selected column
    return render(request, 'reviews/thank_you.html',{
        'latest_username' : latest_username.user_name  # select lastest 'user_name'
    })