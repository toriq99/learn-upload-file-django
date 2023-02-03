from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('thank-you/', views.thankyou),
    path('review-list/', views.ReviewListView.as_view()),
    path('review-list/<int:pk>', views.SingleReviewView.as_view()),
]
