from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView

from .forms import MyForm
from .models import Review

# Create your views here.

# ReviewView using FormView
class ReviewView(FormView):
    form_class = MyForm
    template_name = "reviews/reviews.html"
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Using custom view
#
# class ReviewView(View):
#     def get(self, request):
#         form = MyForm()
        
#         return render(request,'reviews/reviews.html', {
#         'form': form
#         })

#     def post(self, request):
#         form = MyForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/thank-you')

def thankyou(request):
    latest_username = Review.objects.latest('user_name') # get latest index selected column
    return render(request, 'reviews/thank_you.html',{
        'latest_username' : latest_username.user_name  # select lastest 'user_name'
    })

class ReviewListView(ListView):
    model = Review
    template_name = "reviews/list_review.html"
    context_object_name = "reviews"  # to retrieve data to view as name reviews
    
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data


# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         review_id = kwargs['id']
#         selected_review = Review.objects.get(pk=review_id)

#         context["reviews"] = selected_review
#         return context
    
class SingleReviewView(DetailView):
    model = Review
    template_name = "reviews/single_review.html"
    context_object_name = "reviews"
