from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_registration),
    path('details/', views.user_details),
    path('referrals/', views.referrals),
]
